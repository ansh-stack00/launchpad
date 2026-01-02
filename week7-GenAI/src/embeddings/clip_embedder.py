import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

class CLIPEmbedder:
    def __init__(self):
        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32",
            
        )
        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32",
            use_fast=True
        )

    def embed_image(self, image_path: str):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            embeddings = self.model.get_image_features(**inputs)
        return embeddings[0].tolist()

    def embed_text(self, text: str):
        inputs = self.processor(text=[text], return_tensors="pt", padding=True)
        with torch.no_grad():
            embeddings = self.model.get_text_features(**inputs)
        return embeddings[0].tolist()
