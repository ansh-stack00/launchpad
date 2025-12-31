from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse
import os
load_dotenv()

print("DEBUG GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )

def get_sparse_embedding_model():
    return FastEmbedSparse(model_name="Qdrant/bm25")