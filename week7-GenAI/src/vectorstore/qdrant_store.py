from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance


def get_qdrant_client():

    COLLECTION_NAME="genai-hestabit"

    client = QdrantClient(
        host="localhost", 
        port=6333
        )
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=768,          
                distance=Distance.COSINE
            )
        )
        print("Collection created")
    return client


# if __name__ == "__main__":
#     client = get_qdrant_client()
#     collections = client.get_collections()

#     for i in collections.collections:
#         print(i.name)
    