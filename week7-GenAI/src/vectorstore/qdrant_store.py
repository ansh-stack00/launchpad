from qdrant_client import QdrantClient


def get_qdrant_client():
    return QdrantClient(
        host="localhost",
        port=6333
    )


if __name__ == "__main__":
    client = get_qdrant_client()
    collections = client.get_collections()
    print("Available collections:", collections)