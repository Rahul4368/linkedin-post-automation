import os
import time
import pandas as pd

from dotenv import load_dotenv
from openai import OpenAI

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv(dotenv_path=".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# =====================================================
# CHECK ENV VARIABLES
# =====================================================

if OPENAI_API_KEY is None:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

if LINKEDIN_EMAIL is None:
    raise ValueError("❌ LINKEDIN_EMAIL not found in .env")

if LINKEDIN_PASSWORD is None:
    raise ValueError("❌ LINKEDIN_PASSWORD not found in .env")

print("✅ ENV Loaded Successfully")

# =====================================================
# OPENAI CLIENT
# =====================================================

client = OpenAI(api_key=OPENAI_API_KEY)

print("✅ OpenAI Loaded Successfully")

# =====================================================
# LOAD CSV FILE
# =====================================================

try:
    df = pd.read_csv("topics.csv")

    print("\n✅ topics.csv Loaded Successfully")
    print(df.head())

except Exception as e:
    print("❌ Error loading CSV:", e)
    exit()

# =====================================================
# SETUP CHROME
# =====================================================

options = webdriver.ChromeOptions()

# Keeps browser open
options.add_experimental_option("detach", True)

# Maximize browser
options.add_argument("--start-maximized")

# Avoid automation detection
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 30)

# =====================================================
# LINKEDIN LOGIN
# =====================================================

try:

    print("\n🌐 Opening LinkedIn Login Page...")

    driver.get("https://www.linkedin.com/login")

    # Email Input
    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    email_input.send_keys(LINKEDIN_EMAIL)

    # Password Input
    password_input = driver.find_element(By.ID, "password")

    password_input.send_keys(LINKEDIN_PASSWORD)

    # Login
    password_input.send_keys(Keys.RETURN)

    print("🔐 Logging into LinkedIn...")

    time.sleep(5)

except Exception as e:

    print("❌ LinkedIn Login Failed:", e)

    driver.quit()
    exit()

# =====================================================
# PROCESS TOPICS
# =====================================================

for index, row in df.iterrows():

    try:

        status = str(row["Status"]).strip().lower()

        if status == "pending":

            topic = row["Topic"]

            print(f"\n🚀 Generating Post For: {topic}")

            # =====================================================
            # PROMPT
            # =====================================================

            prompt = f"""
            You are a professional LinkedIn content writer.

            Write a professional and engaging LinkedIn post about:

            {topic}

            Requirements:
            - Professional tone
            - Human-like writing
            - 150-200 words
            - Add emojis
            - Add CTA
            - Add hashtags
            - Make it engaging
            """

            # =====================================================
            # GENERATE POST
            # =====================================================

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            post = response.choices[0].message.content

            print("\n📝 Generated Post:\n")
            print(post)

            # =====================================================
            # SAVE GENERATED POST
            # =====================================================

            with open(
                "generated_posts.txt",
                "a",
                encoding="utf-8"
            ) as file:

                file.write(post)
                file.write("\n\n========================\n\n")

            print("✅ Post Saved Successfully")

            # =====================================================
            # OPEN LINKEDIN FEED
            # =====================================================

            driver.get("https://www.linkedin.com/feed/")

            time.sleep(5)

            print("📢 Opening LinkedIn Post Box...")

            # =====================================================
            # CLICK START POST BUTTON
            # =====================================================

            start_post = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(., 'Start a post')]"
                    )
                )
            )

            start_post.click()

            time.sleep(3)

            # =====================================================
            # WRITE POST
            # =====================================================

            print("✍️ Writing Post...")

            post_box = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[@role='textbox']"
                    )
                )
            )

            post_box.send_keys(post)

            time.sleep(3)

            # =====================================================
            # CLICK POST BUTTON
            # =====================================================

            print("📤 Publishing Post...")

            post_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(@aria-label,'Post')]"
                    )
                )
            )

            post_button.click()

            print("✅ Post Published Successfully!")

            # =====================================================
            # UPDATE CSV STATUS
            # =====================================================

            df.at[index, "Status"] = "Done"

            df.to_csv("topics.csv", index=False)

            print(f"✅ Topic '{topic}' Completed")

            time.sleep(5)

    except Exception as e:

        print(f"❌ Error Processing Topic: {e}")

        continue

# =====================================================
# FINISHED
# =====================================================

print("\n🎉 All Automation Completed Successfully!")

# Optional
# driver.quit()