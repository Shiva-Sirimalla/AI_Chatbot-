from collections import deque
from typing import Deque, Iterator

from openai import OpenAI

from config import Settings


SYSTEM_PROMPT = (
    "You are a helpful, friendly AI assistant. "
    "Answer clearly and concisely unless the user asks for detail."
)


class ChatBot:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = OpenAI(api_key=settings.api_key, base_url=settings.base_url)
        self.history: Deque[dict[str, str]] = deque(maxlen=settings.max_history * 2)
        self.history.append({"role": "system", "content": SYSTEM_PROMPT})

    def clear_history(self) -> None:
        self.history.clear()
        self.history.append({"role": "system", "content": SYSTEM_PROMPT})

    def _trim_history(self) -> None:
        system = self.history[0]
        messages = list(self.history)[1:]
        if len(messages) > self.settings.max_history * 2:
            messages = messages[-(self.settings.max_history * 2) :]
        self.history.clear()
        self.history.append(system)
        self.history.extend(messages)

    def chat(self, user_message: str, stream: bool = True) -> str | Iterator[str]:
        self.history.append({"role": "user", "content": user_message})
        self._trim_history()

        if stream:
            return self._stream_reply()

        response = self.client.chat.completions.create(
            model=self.settings.model,
            messages=list(self.history),
            stream=False,
        )
        reply = response.choices[0].message.content or ""
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def _stream_reply(self) -> Iterator[str]:
        stream = self.client.chat.completions.create(
            model=self.settings.model,
            messages=list(self.history),
            stream=True,
        )

        chunks: list[str] = []
        for event in stream:
            delta = event.choices[0].delta.content
            if delta:
                chunks.append(delta)
                yield delta

        reply = "".join(chunks)
        self.history.append({"role": "assistant", "content": reply})
