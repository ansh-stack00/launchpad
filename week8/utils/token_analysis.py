import json
import matplotlib.pyplot as plt
from transformers import AutoTokenizer
import os 

DATA_PATH = "data/train.jsonl"
OUTPUT_DIR = "analysis"
OUTPUT_PLOT = os.path.join(OUTPUT_DIR, "token_length_distribution.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)


tokenizer = AutoTokenizer.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

lengths = []

with open("data/train.jsonl") as f:
    for line in f:
        obj = json.loads(line)
        text = f"{obj['instruction']} {obj['input']} {obj['output']}"
        tokens = tokenizer(text, truncation=False)["input_ids"]
        lengths.append(len(tokens))

# Plot distribution
plt.figure(figsize=(10, 6))
plt.hist(lengths, bins=50)
plt.xlabel("Token Length")
plt.ylabel("Frequency")
plt.title("Token Length Distribution (Finance Dataset)")
plt.grid(True)
plt.savefig(OUTPUT_PLOT, dpi=300, bbox_inches="tight")
plt.close()


print(f"Saved plot to: {OUTPUT_PLOT}")
print(f"Total samples analyzed: {len(lengths)}")
print(f"Average token length: {sum(lengths) / len(lengths):.2f}")
print(f"Max token length: {max(lengths)}")
print(f"Min token length: {min(lengths)}")