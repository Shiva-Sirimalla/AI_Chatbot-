import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

GROQ_BASE_URL = "https://api.groq.com/openai/v1"


@dataclass(frozen=True)
class ServerSettings:
    app_host: str = "127.0.0.1"
    app_port: int = 8501


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str
    base_url: str = GROQ_BASE_URL
    max_history: int = 20
    app_host: str = "127.0.0.1"
    app_port: int = 8501


def load_server_settings() -> ServerSettings:
    app_host = os.getenv("APP_HOST", "127.0.0.1").strip() or "127.0.0.1"
    app_port = int(os.getenv("APP_PORT", "8501"))
    return ServerSettings(app_host=app_host, app_port=app_port)


def load_settings() -> Settings:
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key or api_key == "your-groq-api-key-here":
        raise ValueError(
            "GROQ_API_KEY is not set. Copy .env.example to .env and add your Groq API key."
        )

    server = load_server_settings()
    model = (
        os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()
        or "llama-3.3-70b-versatile"
    )
    max_history = int(os.getenv("MAX_HISTORY", "20"))
    base_url = os.getenv("GROQ_BASE_URL", GROQ_BASE_URL).strip() or GROQ_BASE_URL

    return Settings(
        api_key=api_key,
        model=model,
        base_url=base_url,
        max_history=max_history,
        app_host=server.app_host,
        app_port=server.app_port,
    )


def app_url(host: str | None = None, port: int | None = None) -> str:
    server = load_server_settings()
    resolved_host = (host or server.app_host).strip() or "127.0.0.1"
    resolved_port = port or server.app_port
    if resolved_host in {"0.0.0.0", "127.0.0.1"}:
        resolved_host = "localhost"
    return f"http://{resolved_host}:{resolved_port}"
