import faiss
import pickle
import os
import numpy as np
import google.generativeai as genai

class VectorStore:
    def __init__(self, dim=768, path="day/memory/faiss"):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.dim = dim
        self.path = path
        self.index_file = os.path.join(path, "index.faiss")
        self.text_file = os.path.join(path, "texts.pkl")
        self.texts = []
        self.init()

    def embed(self, text: str):
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text
        )
        emb = np.array(result["embedding"], dtype="float32")

        # Normalize for cosine similarity (important for IndexFlatIP)
        emb = emb / np.linalg.norm(emb)
        return emb

    def init(self):
        os.makedirs(self.path, exist_ok=True)

        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)

            if os.path.exists(self.text_file):
                with open(self.text_file, "rb") as f:
                    self.texts = pickle.load(f)
            else:
                self.texts = []
        else:
            self.index = faiss.IndexFlatIP(self.dim)
            self.texts = []

    def add(self, text: str):
        embedding = self.embed(text)
        self.index.add(np.array([embedding]))
        self.texts.append(text)

    def search(self, query: str, k=5):
        if self.index.ntotal == 0:
            return []

        embedding = self.embed(query)
        _, idxs = self.index.search(np.array([embedding]), k)

        return [
            self.texts[i]
            for i in idxs[0]
            if 0 <= i < len(self.texts)
        ]

    def save(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.text_file, "wb") as f:
            pickle.dump(self.texts, f)
