from src.pipelines.load_documents import load_doc
from src.pipelines.chunks_document import chunk_docs
from src.embeddings.embedder import (get_embedding_model,get_sparse_embedding_model)
from src.vectorstore.qdrant_store import get_qdrant_client
from langchain_qdrant import QdrantVectorStore


if __name__=="__main__":
    docs = load_doc()
    chunks = chunk_docs(docs)

    print(f"Total chunks: {len(chunks)}")

    embeddings = get_embedding_model()
    client = get_qdrant_client()

# creating vectorstore
    vectorstore = QdrantVectorStore(
        client=client,
        embedding=embeddings,
        collection_name="genai-hestabit",
        vector_name="dense",
    )

    vectorstore.add_documents(
        chunks,
        batch_size=64
    )

# Sparse indexing
    sparse_embeddings = get_sparse_embedding_model()
    vectorstore_sparse = QdrantVectorStore(
        client=client,
        embedding=sparse_embeddings,
        collection_name="genai-hestabit",
        vector_name="sparse"
    )
    vectorstore_sparse.add_documents(chunks, batch_size=64)
    print("Sparse indexing done.")


    print("indexing is done (sparse + dense)...")
    