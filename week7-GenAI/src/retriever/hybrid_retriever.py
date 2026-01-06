from src.embeddings.embedder import get_embedding_model, get_sparse_embedding_model
from src.generator.llm_client import get_llm
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from src.utils.re_ranker import rerank
from src.evaluation.hallucination_detector import detect_hallucination


from src.memory.memory_store import (
    init_memory,
    add_user_message,
    add_assistant_message,
    get_memory
)

load_dotenv()

embedding_model = get_embedding_model()
sparse_embedding=get_sparse_embedding_model()

client = get_llm()

# initializing short term memory 
init_memory(max_turns=5)



vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="my_documents",
    embedding=embedding_model,
    sparse_embedding=sparse_embedding
)

while True:
    user_query = input("\nAsk something or (type exit): ")

    if user_query.lower() == "exit":
        break

# adding user message into memory 
    add_user_message(user_query)

    initial_results = vector_db.similarity_search(query=user_query, k=10)
    # print("intital search",initial_results)

    # reranking the searched results
    search_results = rerank(query=user_query, docs=initial_results,top_k=3)
    # print("after reranking", search_results)

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

    messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            }
        ]
    messages.extend(get_memory())


    responses = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
        
    )

    assitant_res = responses.choices[0].message.content

    is_hallucinated, score = detect_hallucination(
        answer=assitant_res,
        context=context
    )

    if is_hallucinated:
        print("\nPotential hallucination detected!")
        print(f"Context Match Score: {score}")
    else:
        print(f"\nFaithful answer (score: {score})")

    print(f"\n🤖 {assitant_res}")

    add_assistant_message(assitant_res)

