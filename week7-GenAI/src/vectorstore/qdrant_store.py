from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    SparseVectorParams,
    Distance
)



# dense vector 
# def get_qdrant_client():

#     COLLECTION_NAME="genai-hestabit"

#     client = QdrantClient(
#         host="localhost", 
#         port=6333
#         )
#     if not client.collection_exists(COLLECTION_NAME):
#         client.create_collection(
#             collection_name=COLLECTION_NAME,
#             vectors_config=VectorParams(
#                 size=768,          
#                 distance=Distance.COSINE
#             )
#         )
#         print("Collection created")
#     return client

def get_qdrant_client():
    COLLECTION_NAME = "genai-hestabit"

    client = QdrantClient(
            host="localhost", 
            port=6333
        )

    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config={
                "dense": VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            },
            sparse_vectors_config={
                "sparse": SparseVectorParams()
            }
        )
        print("Hybrid collection created")

    return client
