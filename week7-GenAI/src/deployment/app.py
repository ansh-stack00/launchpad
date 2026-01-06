from fastapi import FastAPI
from pydantic import BaseModel
from src.retriever.hybrid_retriever import ask_rag
from src.evaluation.human_feedback import log_human_feedback

app = FastAPI(title="Advanced RAG API")

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    hallucinated: bool

@app.post("/ask", response_model=AskResponse)
def ask_endpoint(data: AskRequest):
    result = ask_rag(data.question)

    log_human_feedback(
        question=data.question,
        answer=result["answer"],
        hallucinated=result["hallucinated"]
    )

    return {
        "answer": result["answer"],
        "hallucinated": result["hallucinated"],
        "sources":result['sources']
    }
