from src.embeddings.embedder import (get_embedding_model,get_sparse_embedding_model)
from src.generator.llm_client import get_llm
from dotenv import load_dotenv
from langchain_qdrant import  RetrievalMode
from langchain_qdrant import QdrantVectorStore


load_dotenv()

embedding_model = get_embedding_model()
sparse_embedding = get_sparse_embedding_model()
client = get_llm()




vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="genai-hestabit",
    embedding=embedding_model,
    sparse_embedding=sparse_embedding,
    vector_name="dense",
    sparse_vector_name="sparse",
    retrieval_mode=RetrievalMode.HYBRID
)

# take user  input

user_query = input("Ask something:")

retriever = vector_db.as_retriever(
    search_kwargs={
        "k": 3,
        
    }
)

search_results =retriever.invoke(user_query)

context ="\n\n\n".join([f"Page Content:{result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Loaction:{result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
You are  helpful AI Assistant who answers user query based on the available context
retrieved from a PDF file along with page_contents and page number.

You should only answer the user based on the following context and navigate the user to 
open the right page number to know more .

context:
{context}

"""


responses = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":user_query
        }
    ]
)

print(f"🤖 {responses.choices[0].message.content}")