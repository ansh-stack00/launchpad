from typing import Dict, List
from fastapi import Request
import  logging
from uuid import uuid4 as uuid
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from deploy.config import DEFAULT_TEMP, DEFAULT_TOP_P, DEFAULT_TOP_K
from deploy.model_loader import load_model

logging.basicConfig(level=logging.INFO)


app = FastAPI(title="Local GGUF LLM API")

llm = load_model()

MAX_TOKENS=256
class GenerateRequest(BaseModel):
    prompt: str
    temperature: float = DEFAULT_TEMP
    top_p: float = DEFAULT_TOP_P
    top_k: int = DEFAULT_TOP_K
    max_tokens: int = MAX_TOKENS
    stream: bool = False


class ChatRequest(BaseModel):
    system_prompt: str = "You are a helpful assistant."
    messages: List[Dict[str, str]] 
    temperature: float = DEFAULT_TEMP
    top_p: float = DEFAULT_TOP_P
    top_k: int = DEFAULT_TOP_K
    max_tokens: int = MAX_TOKENS
    stream: bool = False



def build_chat_prompt(system_prompt, messages):
    prompt = f"### System:\n{system_prompt}\n\n"
    for m in messages:
        role = m["role"].capitalize()
        prompt += f"### {role}:\n{m['content']}\n\n"
    prompt += "### Assistant:\n"
    return prompt


def stream_tokens(prompt, **kwargs):
    stream = llm(prompt, stream=True, **kwargs)
    for output in stream:
        token = output["choices"][0]["text"]
        yield token



@app.post("/generate")
def generate(req: GenerateRequest, request: Request):
    request_id = str(uuid())
    logging.info(f"[{request_id}] /generate called")

    params = dict(
        max_tokens=req.max_tokens,
        temperature=req.temperature,
        top_p=req.top_p,
        top_k=req.top_k,
    )

    if req.stream:
        return StreamingResponse(
            stream_tokens(req.prompt, **params),
            media_type="text/plain"
        )

    output = llm(req.prompt, **params)

    return {
        "request_id": request_id,
        "output": output["choices"][0]["text"]
    }


@app.post("/chat")
def chat(req: ChatRequest):
    request_id = str(uuid())
    logging.info(f"[{request_id}] /chat called")

    prompt = build_chat_prompt(req.system_prompt, req.messages)

    params = dict(
        max_tokens=req.max_tokens,
        temperature=req.temperature,
        top_p=req.top_p,
        top_k=req.top_k,
    )

    if req.stream:
        return StreamingResponse(
            stream_tokens(prompt, **params),
            media_type="text/plain"
        )

    output = llm(prompt, **params)

    return {
        "request_id": request_id,
        "reply": output["choices"][0]["text"]
    }