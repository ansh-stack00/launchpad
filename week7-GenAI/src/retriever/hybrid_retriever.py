from src.embeddings.embedder import get_embedding_model, get_sparse_embedding_model
from src.generator.llm_client import get_llm
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore


load_dotenv()

embedding_model = get_embedding_model()
sparse_embedding=get_sparse_embedding_model()

client = get_llm()



vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="my_documents",
    embedding=embedding_model,
    sparse_embedding=sparse_embedding
)

# take user  input

user_query = input("Ask something:")

search_results = vector_db.similarity_search(query=user_query, k=3)

context ="\n\n\n".join([f"Page Content:{result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Loaction:{result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
You are  helpful AI Assistant who answers user query based on the available context
retrieved from a PDF file along with page_contents and page number.

You should only answer the user based on the following context and navigate the user to 
open the right page number to know more .

If user asks anything which is not in context . Just say sorry .

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