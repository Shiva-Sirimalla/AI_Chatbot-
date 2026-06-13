# Groq AI Chatbot

A Python chatbot with a Streamlit web UI, powered by the Groq API.

## Features

- Real-time streaming responses
- Conversation memory during each session
- Groq API integration (OpenAI-compatible client)
- Simple web UI built with Streamlit
- Environment-based configuration with `.env`

## Tech Stack

- Python
- Streamlit
- Groq API
- OpenAI Python SDK

## Project Structure

```
app.py        # Streamlit UI
chatbot.py    # Chat logic and API calls
config.py     # Environment settings
run.py        # Start the web app
main.py       # Optional CLI version
start.bat     # Windows one-click launcher
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Shiva-Sirimalla/groq-chatbot.git
cd groq-chatbot
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Create your environment file:

```bash
copy .env.example .env
```

4. Add your Groq API key to `.env`:

```env
GROQ_API_KEY=your-groq-api-key-here
GROQ_MODEL=llama-3.3-70b-versatile
```

Get a key from [console.groq.com](https://console.groq.com).

## Run the App

### Windows

Double-click `start.bat` or run:

```bash
python run.py
```

Then open:

```text
http://localhost:8501
```

### CLI mode

```bash
python main.py
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Groq API key | required |
| `GROQ_MODEL` | Groq model name | `llama-3.3-70b-versatile` |
| `APP_HOST` | Server host | `127.0.0.1` |
| `APP_PORT` | Server port | `8501` |
| `MAX_HISTORY` | Conversation turns to keep | `20` |

## Notes

- Keep the terminal open while using the Streamlit app.
- Never commit your `.env` file or API keys to GitHub.

## Author

Fresher portfolio project — Python AI chatbot with Groq and Streamlit.
