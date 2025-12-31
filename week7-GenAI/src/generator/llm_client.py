from openai import OpenAI

def get_llm():
    return  OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=""
    )