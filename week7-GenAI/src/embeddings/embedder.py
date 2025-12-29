from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
load_dotenv()

print("DEBUG GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )

if __name__ == "__main__":
    embedder = get_embedding_model()

    # embedding the sample data 
    vector = embedder.embed_query("This is a test sentence")
    print("Vector length:", len(vector))
    print("First 10 values:", vector[:10])
