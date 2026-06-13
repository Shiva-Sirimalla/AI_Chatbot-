import sys

from chatbot import ChatBot
from config import load_settings


def print_banner() -> None:
    print("=" * 50)
    print("  Groq Chatbot")
    print("=" * 50)
    print("Commands: /quit  /clear  /help")
    print("-" * 50)


def print_help() -> None:
    print(
        "\nCommands:\n"
        "  /quit   Exit the chatbot\n"
        "  /clear  Clear conversation history\n"
        "  /help   Show this help message\n"
    )


def run() -> None:
    try:
        settings = load_settings()
    except ValueError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        sys.exit(1)

    bot = ChatBot(settings)
    print_banner()

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        command = user_input.lower()
        if command in {"/quit", "/exit", "/q"}:
            print("Goodbye!")
            break
        if command == "/clear":
            bot.clear_history()
            print("Conversation cleared.")
            continue
        if command == "/help":
            print_help()
            continue

        print("\nBot: ", end="", flush=True)
        try:
            for chunk in bot.chat(user_input, stream=True):
                print(chunk, end="", flush=True)
            print()
        except Exception as exc:
            print(f"\nError: {exc}", file=sys.stderr)
            if bot.history and bot.history[-1]["role"] == "user":
                bot.history.pop()


if __name__ == "__main__":
    run()
