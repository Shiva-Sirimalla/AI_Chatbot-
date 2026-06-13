# AI Chatbot

AI-powered conversational chatbot built with **Python**, **Streamlit**, and the **Groq API** (Llama 3.3). Supports real-time streaming responses, session-based conversation memory, and a clean web chat interface.

**Repository:** https://github.com/Shiva-Sirimalla/AI_Chatbot-

## About This Project

This project is a full-stack AI chatbot application that lets users chat with a large language model through a simple browser UI. It uses Groq's fast inference API with the Llama 3.3 model to generate helpful, conversational replies in real time.

The app is designed as a **fresher portfolio project** and demonstrates practical skills in Python development, API integration, environment configuration, and building interactive web apps with Streamlit.

### What It Does

- Accepts user messages through a Streamlit chat interface
- Sends prompts to Groq's Llama 3.3 model
- Streams AI responses word-by-word for a smooth chat experience
- Remembers recent conversation context during a session
- Supports both **web UI** and **CLI** modes

### Why I Built This

To practice building a real AI application from scratch — connecting a frontend UI to an LLM API, handling streaming output, managing chat history, and structuring a clean Python project for deployment and portfolio use.

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
git clone https://github.com/Shiva-Sirimalla/AI_Chatbot-.git
cd AI_Chatbot-
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

**Shiva Sirimalla** — Fresher portfolio project showcasing Python, Groq API, and Streamlit.

## GitHub About Description

Use this short text in your repo **About** section on GitHub:

```text
AI-powered chatbot using Python, Streamlit, and Groq Llama 3.3. Real-time streaming responses, session memory, CLI + web UI. Fresher portfolio project.
```

Suggested topics: `python` `streamlit` `groq` `llama` `chatbot` `ai` `generative-ai` `llm`
