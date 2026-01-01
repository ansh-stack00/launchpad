from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

def get_llm():
    return  OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("api_key")
    )