import streamlit as st

from chatbot import ChatBot
from config import load_settings


def init_session() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "bot" not in st.session_state:
        try:
            settings = load_settings()
            st.session_state.bot = ChatBot(settings)
            st.session_state.settings = settings
            st.session_state.config_error = None
        except ValueError as exc:
            st.session_state.bot = None
            st.session_state.settings = None
            st.session_state.config_error = str(exc)


def clear_chat() -> None:
    st.session_state.messages = []
    if st.session_state.bot:
        st.session_state.bot.clear_history()


def render_sidebar() -> None:
    with st.sidebar:
        st.title("Settings")

        if st.session_state.config_error:
            st.error(st.session_state.config_error)
            st.caption("Add your Groq API key to the `.env` file, then refresh this page.")
        elif st.session_state.settings:
            st.success("Connected to Groq")
            st.text(f"Model: {st.session_state.settings.model}")
            st.text(f"Max history: {st.session_state.settings.max_history} turns")

        st.info("If this page loaded, the link is working.")

        st.divider()

        if st.button("Clear chat", use_container_width=True):
            clear_chat()
            st.rerun()

        st.caption("Powered by Groq + Streamlit")


def render_chat() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Message the assistant..."):
        if not st.session_state.bot:
            st.error(st.session_state.config_error or "Chatbot is not configured.")
            return

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                stream = st.session_state.bot.chat(prompt, stream=True)
                response = st.write_stream(stream)
            except Exception as exc:
                st.error(f"Something went wrong: {exc}")
                if (
                    st.session_state.bot.history
                    and st.session_state.bot.history[-1]["role"] == "user"
                ):
                    st.session_state.bot.history.pop()
                st.session_state.messages.pop()
                return

        st.session_state.messages.append({"role": "assistant", "content": response})


def main() -> None:
    st.set_page_config(
        page_title="Groq Chatbot",
        page_icon="💬",
        layout="centered",
    )

    init_session()
    render_sidebar()

    st.title("Groq Chatbot")
    st.caption("Ask anything. Your conversation stays in this session.")

    if not st.session_state.messages:
        st.markdown("Welcome! Type your first message in the box below.")

    render_chat()


main()