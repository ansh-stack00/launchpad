from src.generator.llm_client import get_llm
from src.retriever.image_search import text_to_image_search

llm = get_llm()

query = "Explain the RAG architecture"

results = text_to_image_search(query)

context = "\n\n".join([
    f"Caption: {r['caption']}\nOCR: {r['ocr_text']}"
    for r in results
])

prompt = f"""
Answer the question using ONLY the following image context:

{context}

Question: {query}
"""

response = llm.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
for r in results:
    r['image'].show()