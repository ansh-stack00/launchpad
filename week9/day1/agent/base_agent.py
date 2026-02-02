from dataclasses import dataclass
from typing import List
from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Message:
    sender: str
    content: str


class Memory:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.messages: List[Message] = []

    def add(self, msg: Message):
        self.messages.append(msg)
        self.messages = self.messages[-self.window_size:]

    def context(self):
        return "\n".join([f"{m.sender}: {m.content}" for m in self.messages])
    
# llm client 
class LocalLLM:
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("api_key")
        )  
        self.model = model

    def generate(self, system_prompt, user_prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content


class BaseAgent:
    def __init__(self, name, system_prompt, llm: LocalLLM, memory_window=10):
        self.name = name
        self.system_prompt = system_prompt
        self.llm = llm
        self.memory = Memory(memory_window)

    def process(self, text: str) -> Message:
        ctx = self.memory.context()

        prompt = f"""
Context:
{ctx}

Input:
{text}
"""

        reply = self.llm.generate(self.system_prompt, prompt)
        msg = Message(self.name, reply)
        self.memory.add(msg)
        return msg
