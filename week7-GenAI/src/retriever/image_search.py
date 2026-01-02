import torch
from PIL import Image
import os
from src.embeddings.clip_embedder import CLIPEmbedder
from src.vectorstore.qdrant_store import get_qdrant_client

clip = CLIPEmbedder()
clip_model = clip.model
clip_processor = clip.processor

client = get_qdrant_client()


def text_to_image_search(query: str, k: int = 3, image_dir="src/data/image_dir"):
   
    with torch.no_grad():
        inputs = clip_processor(text=query, return_tensors="pt")
        vector = clip_model.get_text_features(**inputs)[0].tolist()

    results = client.query_points(
        collection_name="genai-hestabit",
        query=vector,
        using="image_dense",       
        with_payload=True,
        limit=k
    )

    output = []
    for r in results.points:
        img_path = os.path.join(image_dir, r.payload['source'])
        try:
            img = Image.open(img_path).convert("RGB")
        except FileNotFoundError:
            print(f"Warning: file not found {img_path}")
            continue

        output.append({
            "image": img,
            "caption": r.payload.get("caption", ""),
            "ocr_text": r.payload.get("ocr_text", ""),
            "source": r.payload.get("source", "")
        })

    return output


def image_to_image_search(image_path: str, k: int = 3, image_dir="src/data/image_dir"):
    """
    Search for images similar to a given image.
    Returns a list of dictionaries with 'image' (PIL.Image), 'caption', 'ocr_text', and 'source'.
    """
    image = Image.open(image_path).convert("RGB")

    with torch.no_grad():
        inputs = clip_processor(images=image, return_tensors="pt")
        vector = clip_model.get_image_features(**inputs)[0].tolist()

    results = client.query_points(
        collection_name="genai-hestabit",
        query=vector,
        using="image_dense",
        with_payload=True,
        limit=k
    )

    output = []
    for r in results.points:
        img_path = os.path.join(image_dir, r.payload['source'])
        try:
            img = Image.open(img_path).convert("RGB")
        except FileNotFoundError:
            print(f"Warning: file not found {img_path}")
            continue

        output.append({
            "image": img,
            "caption": r.payload.get("caption", ""),
            "ocr_text": r.payload.get("ocr_text", ""),
            "source": r.payload.get("source", "")
        })

    return output
