import os
import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def ensure_env_file() -> None:
    env_path = Path(__file__).resolve().parent / ".env"
    example_path = Path(__file__).resolve().parent / ".env.example"

    if env_path.exists() or not example_path.exists():
        return

    import shutil

    shutil.copy(example_path, env_path)
    load_dotenv(env_path, override=True)
    print("Created .env from .env.example. Add your Groq API key if chat does not work.")


def pick_port(host: str, preferred: int) -> int:
    for port in (preferred, 8501, 8080, 8502, 8503):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free port found. Close other Streamlit apps and try again.")


def open_browser(url: str) -> None:
    time.sleep(2)
    webbrowser.open(url)


def main() -> None:
    ensure_env_file()

    from config import app_url, load_server_settings

    settings = load_server_settings()
    host = "127.0.0.1"
    port = pick_port(host, settings.app_port)
    app_path = Path(__file__).resolve().parent / "app.py"
    url = app_url("localhost", port)
    port_file = Path(__file__).resolve().parent / ".app_port"
    port_file.write_text(str(port), encoding="utf-8")

    print("=" * 50)
    print("  Groq Chatbot")
    print("=" * 50)
    print(f"Open this link in your browser:\n  {url}\n")
    print("Keep this window open while you use the chatbot.")
    print("Press Ctrl+C to stop.")
    print("=" * 50, flush=True)

    import threading

    threading.Thread(target=open_browser, args=(url,), daemon=True).start()

    command = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(app_path),
        "--server.address",
        host,
        "--server.port",
        str(port),
        "--browser.serverAddress",
        "localhost",
        "--server.headless",
        "false",
    ]

    raise SystemExit(subprocess.call(command))


if __name__ == "__main__":
    main()
