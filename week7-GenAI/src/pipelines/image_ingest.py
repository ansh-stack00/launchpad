import os
import pytesseract
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from src.vectorstore.qdrant_store import get_qdrant_client
from src.embeddings.clip_embedder import CLIPEmbedder

blip_processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
blip_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

clip = CLIPEmbedder()

def generate_caption(image: Image.Image):
    inputs = blip_processor(image, return_tensors="pt")
    out = blip_model.generate(**inputs)
    return blip_processor.decode(out[0], skip_special_tokens=True)

def ingest_images(image_dir: str):
    client = get_qdrant_client()
    for file in os.listdir(image_dir):
        if not file.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        path = os.path.join(image_dir, file)
        image = Image.open(path).convert("RGB")

        ocr_text = pytesseract.image_to_string(image)
        caption = generate_caption(image)
        clip_vector = clip.embed_image(path)

        client.upsert(
            collection_name="genai-hestabit",
            points=[{
                "id": hash(file),
                "vector": {
                    "image_dense": clip_vector
                },
                "payload": {
                    "ocr_text": ocr_text,
                    "caption": caption,
                    "source": file
                }
            }]
        )

        print(f"Ingested {file}")
if __name__=="__main__":
    ingest_images("src/data/image_dir")