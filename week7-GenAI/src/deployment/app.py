from fastapi import FastAPI
from pydantic import BaseModel
from src.retriever.hybrid_retriever import ask_rag
from src.evaluation.human_feedback import log_human_feedback
from src.pipelines.sql_pipeline import ask_sql

app = FastAPI(title="Advanced RAG API")

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    hallucinated: bool

class AskSQLResponse(BaseModel):
    sql: str | None = None
    columns: list | None = None
    rows: list | None = None
    summary: str | None = None
    error: str | None = None


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

@app.post("/ask-sql", response_model=AskSQLResponse)
def ask_sql_endpoint(data: AskRequest):
    result = ask_sql(data.question)

    return result


