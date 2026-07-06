
# LinkedIn Post Automation Using OpenAI and Selenium

An AI-powered automation project that generates professional LinkedIn posts from predefined topics and automatically publishes them using browser automation.

The project reads topics from a CSV file, generates engaging content using the OpenAI API, saves generated posts locally, publishes them on LinkedIn through Selenium, and updates the topic status after successful processing.

## Features

* AI-generated LinkedIn posts
* Topic management using CSV
* Automated LinkedIn login
* Automatic post creation and publishing
* Environment variable support for credentials
* Generated post backup in a text file
* Automatic topic status updates
* Error handling for individual topics
* Multiple topic processing in a single run

## Tech Stack

* Python
* OpenAI API
* Selenium WebDriver
* Pandas
* python-dotenv
* webdriver-manager
* Google Chrome

## Project Structure

```text
linkedin-post-automation/
│
├── linkedin/
│   ├── app.py
│   ├── topics.csv
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

After running the application, a `generated_posts.txt` file is automatically created to store generated LinkedIn posts.

## Workflow

```text
topics.csv
     |
     v
Read Pending Topic
     |
     v
Generate LinkedIn Post with OpenAI
     |
     v
Save Generated Post
     |
     v
Open LinkedIn with Selenium
     |
     v
Login to LinkedIn
     |
     v
Create and Publish Post
     |
     v
Update CSV Status to Done
```

## Prerequisites

Before running the project, make sure you have:

* Python 3.9 or higher
* Google Chrome installed
* OpenAI API key
* LinkedIn account
* Stable internet connection

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd linkedin-post-automation/linkedin
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file inside the folder where `app.py` is located.

```env
OPENAI_API_KEY=your_openai_api_key
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password
```

Never upload the `.env` file to GitHub or any public repository.

Add the following entries to `.gitignore`:

```text
.env
venv/
__pycache__/
generated_posts.txt
```

## topics.csv Format

Create or update the `topics.csv` file using the following format:

```csv
Topic,Status
Machine Learning Career Roadmap,Pending
Introduction to Generative AI,Pending
Importance of Python for Data Science,Pending
RAG Applications in AI,Pending
```

The application processes only topics where the `Status` value is `Pending`.

After successful processing, the status is automatically changed:

```csv
Topic,Status
Machine Learning Career Roadmap,Done
Introduction to Generative AI,Pending
Importance of Python for Data Science,Pending
RAG Applications in AI,Pending
```

## Running the Project

Run the application using:

```bash
python app.py
```

The automation will:

1. Load environment variables.
2. Read topics from `topics.csv`.
3. Open Google Chrome.
4. Log in to LinkedIn.
5. Find topics marked as `Pending`.
6. Generate a professional LinkedIn post using OpenAI.
7. Save the generated content in `generated_posts.txt`.
8. Open the LinkedIn post editor.
9. Enter the generated content.
10. Publish the post.
11. Change the topic status from `Pending` to `Done`.

## requirements.txt

The project requires the following Python packages:

```text
openai
selenium
pandas
python-dotenv
webdriver-manager
```

Install them with:

```bash
pip install -r requirements.txt
```

## AI Content Generation

The project uses the OpenAI API to generate professional LinkedIn content.

The prompt instructs the model to generate posts with:

* Professional tone
* Human-like writing
* Approximately 150–200 words
* Relevant emojis
* A call to action
* Relevant hashtags
* Engaging and readable formatting

The model configured in the current application is:

```text
gpt-4.1-mini
```

## Error Handling

The application includes error handling for:

* Missing environment variables
* Invalid or missing API keys
* CSV loading errors
* LinkedIn login failures
* Selenium element detection failures
* Post generation errors
* Individual topic processing errors

If one topic fails during processing, the application logs the error and continues with the next available topic.

## Security Recommendations

* Never commit `.env` to a public repository.
* Never hardcode API keys or passwords in Python files.
* Use environment variables for sensitive credentials.
* Rotate credentials immediately if they are accidentally exposed.
* Avoid storing production credentials in shared development environments.

## Important Note

LinkedIn may change its interface, authentication flow, or HTML structure. Selenium selectors used in this project may require updates when the website UI changes.

Automated activity may also be subject to LinkedIn's platform rules and usage restrictions. Use this project responsibly and review applicable platform policies before using automated publishing in production.

## Future Improvements

Possible improvements include:

* Streamlit dashboard for topic management
* Scheduled post publishing
* Image generation for LinkedIn posts
* Post approval workflow before publishing
* Multiple content styles
* Database integration
* Retry mechanism for failed posts
* Logging system
* Docker support
* Cloud deployment
* LinkedIn API integration where available and appropriate
* Analytics dashboard for post performance

## Learning Outcomes

This project demonstrates practical experience with:

* Generative AI API integration
* Prompt engineering
* Browser automation
* Selenium WebDriver
* CSV-based workflow management
* Environment variable management
* Python exception handling
* AI-powered content automation

## Disclaimer

This project is intended for educational and portfolio purposes. Users are responsible for ensuring that their use of automation complies with applicable platform terms, account security requirements, and relevant policies.

## Author

**Rahul Kumar**

AI/ML and Python Developer interested in Machine Learning, Generative AI, RAG systems, FastAPI, automation, and intelligent application development.

## License

This project can be used for learning and educational purposes. Add a formal license file if you plan to distribute or reuse the project publicly.
