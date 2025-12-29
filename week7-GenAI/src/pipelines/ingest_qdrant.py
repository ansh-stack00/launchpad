from src.pipelines.load_documents import load_doc
from src.pipelines.chunks_document import chunk_docs
from src.embeddings.embedder import get_embedding_model
# from src.vectorstore.qdrant_store import get_qdrant_client
from langchain_qdrant import QdrantVectorStore




COLLECTION_NAME="enterprise_docs"

if __name__=="__main__":
    docs = load_doc()
    chunks = chunk_docs(docs)

    print(f"Total chunks: {len(chunks)}")

    embeddings = get_embedding_model()
    # client = get_qdrant_client()

# creating vectorstore
    vectorstore = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
    )


    print("indexing is done...")
