%%writefile test_inference.py
import torch
import time
import csv
import os
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "finetuned"  
# MODEL_PATH = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
MODEL_PATH = "merged/merged_model"

PROMPT = """
<|user|>
Instruction: Calculate overhead rate.
Input: Total manufacturing overhead: $200,000, Direct labor hours: 10,000.
<|assistant|>
"""

MAX_NEW_TOKENS = 120
RESULTS_FILE = "benchmarks/results.csv"


device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto"
)

inputs = tokenizer(PROMPT, return_tensors="pt").to(device)


torch.cuda.empty_cache()
start = time.time()

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=MAX_NEW_TOKENS,
        do_sample=False
    )

end = time.time()

tokens_generated = outputs.shape[1] - inputs["input_ids"].shape[1]
latency = end - start
tokens_per_sec = tokens_generated / latency

vram_used = None
if torch.cuda.is_available():
    vram_used = torch.cuda.max_memory_allocated() / 1024**2 

output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\n.... OUTPUT ...")
print(output_text)
print("end")

print(f"Model: {MODEL_NAME}")
print(f"Tokens generated: {tokens_generated}")
print(f"Latency (s): {latency:.2f}")
print(f"Tokens/sec: {tokens_per_sec:.2f}")
print(f"VRAM used (MB): {vram_used}")


os.makedirs("../benchmarks", exist_ok=True)
file_exists = os.path.isfile(RESULTS_FILE)

with open(RESULTS_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow([
            "model",
            "device",
            "tokens_generated",
            "latency_sec",
            "tokens_per_sec",
            "vram_mb"
        ])
    writer.writerow([
        MODEL_NAME,
        device,
        tokens_generated,
        round(latency, 3),
        round(tokens_per_sec, 2),
        round(vram_used, 2) if vram_used else "CPU"
    ])
