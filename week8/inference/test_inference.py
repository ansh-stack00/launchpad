import time
import torch
import psutil
import pandas as pd
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer, util


GGUF_MODEL = "./quantized/model.gguf"
PROMPTS = [
    """### Instruction:
Answer the medical question accurately.

### Input:
What are the treatments for Heart Attack ?

### Response:
""",

    """### Instruction:
Answer the medical question accurately.

### Input:
What is (are) Low Vision ?

### Response:
""",

    """### Instruction:
Answer the medical question accurately.

### Input:
Is Ovarian Epithelial, Fallopian Tube, and Primary Peritoneal Cancer inherited ?

### Response:
"""
]


GROUND_TRUTH = [
    "Heart attack treatment focuses on quickly restoring blood flow using thrombolytic drugs or angioplasty, followed by cardiac rehabilitation, lifestyle changes, and medications to prevent further damage.",

    "People with low vision can receive support services such as vision rehabilitation, counseling, recreation programs, and job training through community and state agencies for the visually impaired.",

    "About 20% of ovarian, fallopian tube, and primary peritoneal cancers are caused by inherited gene mutations, often associated with breast or colon cancer, and genetic testing is recommended for high-risk families."
]


embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def get_vram():
    if torch.cuda.is_available():
        return torch.cuda.memory_allocated() / 1024**2
    return 0

def accuracy(preds, refs):
    p_emb = embedder.encode(preds, convert_to_tensor=True)
    r_emb = embedder.encode(refs, convert_to_tensor=True)

    sims = util.cos_sim(p_emb, r_emb)

    per_sample_scores = sims.diag().cpu().numpy()

    # for i, score in enumerate(per_sample_scores):
    #     print(f"Sample {i+1} Similarity: {score:.3f}")

    mean_score = per_sample_scores.mean()

    return mean_score




def benchmark_gguf(label):
    llm = Llama(model_path=GGUF_MODEL, n_ctx=2048, n_threads=8, verbose=False)

    outputs = []
    start = time.time()

    for p in PROMPTS:
        response = ""
        stream = llm(p, max_tokens=256, stream=True)

        for output in stream:
            token = output["choices"][0]["text"]
            response += token
            # print(token, end="", flush=True)

        # print("\n \n")
        outputs.append(response)

    end = time.time()

    tokens = sum(len(o.split()) for o in outputs)
    tps = tokens / (end - start)
    acc = accuracy(outputs, GROUND_TRUTH)

    return {
        "Model": label,
        "Tokens/sec": round(tps, 2),
        "Latency(s)": round(end - start, 2),
        "VRAM(MB)": 0,
        "Accuracy": round(acc, 3)
    }

results = []

results.append(benchmark_gguf("GGUF Q4 llama.cpp"))


from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer

import threading

BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
FT_MODEL = "./quantized/fp16-merged"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
RESULTS_PATH = "results.csv"



def benchmark_hf(model_path, label):
        
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map=DEVICE)

    outputs = []
    start = time.time()

    for prompt in PROMPTS:
        streamer = TextIteratorStreamer(tokenizer, skip_special_tokens=True)
        inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)

        generation_kwargs = dict(
            **inputs,
            max_new_tokens=256,
            streamer=streamer,
            pad_token_id=tokenizer.eos_token_id 
        )

        thread = threading.Thread(target=model.generate, kwargs=generation_kwargs)
        thread.start()

        response = ""
        for token in streamer:
            response += token
        #     print(token, end="", flush=True)

        # print("\n \n")
        outputs.append(response)
        thread.join()

    end = time.time()

    total_tokens = sum(len(tokenizer.encode(r)) for r in outputs)
    duration = end - start
    tps = total_tokens / duration
    acc = accuracy(outputs, GROUND_TRUTH)

    return {
        "Model": label,
        "Tokens/sec": round(tps, 2),
        "Latency(s)": round(duration, 2),
        "VRAM(MB)": round(get_vram(), 2),
        "Accuracy": round(acc, 3)
    }


results.append(benchmark_hf(BASE_MODEL, "Base Model"))
results.append(benchmark_hf(FT_MODEL, "Fine-tuned"))

df = pd.DataFrame(results)
df.to_csv(RESULTS_PATH, index=False)

print(df)