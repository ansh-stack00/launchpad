# Quantisation Report (DAY 3)

## Model Overview
- **Base Model:** TinyLlama/TinyLlama-1.1B-Chat-v1.0  
- **Fine-tuning Method:** QLoRA (instruction–input–output format)  
- **LoRA Config:** r=16, alpha=32, dropout=0.05  
- **Training Precision:** 4-bit NF4 (bitsandbytes)  

Before quantisation, the LoRA adapter was **merged into the base model** to produce a standalone FP16 model suitable for post-training quantisation.

---

## Quantisation Objectives
- Reduce model memory footprint
- Improve inference speed
- Enable deployment on low-resource hardware (GPU & CPU)
- Compare memory–speed–quality trade-offs

---

## Quantisation Methods Used

### 1. FP16 (Baseline)
- Format: FP16 Hugging Face model
- Purpose: Quality reference
- Hardware: GPU

### 2. INT8 Quantisation
- Method: Post-training dynamic quantisation
- Tool: bitsandbytes (8-bit)
- Hardware: GPU
- Goal: Reduce memory with minimal quality loss

### 3. INT4 Quantisation
- Method: Post-training 4-bit quantisation
- Tool: bitsandbytes (NF4 + double quant)
- Hardware: GPU
- Goal: Maximum memory savings on GPU

### 4. GGUF Quantisation
- Toolchain: llama.cpp (CMake build)
- Conversion: Hugging Face → FP16 GGUF
- Quantisation: `llama-quantize`
- Formats evaluated:
  - q4_0 (smaller, faster)
  - q8_0 (higher quality)
- Hardware: CPU / edge devices

---

## Size Comparison

| Format        | Approx Size | Memory Reduction |
|---------------|-------------|------------------|
| FP16          | ~2.2 GB     | Baseline         |
| INT8          | ~1.1 GB     | ~50%             |
| INT4          | ~600 MB     | ~72%             |
| GGUF (q4_0)   | ~500 MB     | ~77%             |
| GGUF (q8_0)   | ~900 MB     | ~59%             |

---

## Speed & Quality Comparison (Qualitative)

| Format      | Inference Speed | Output Quality |
|------------|-----------------|----------------|
| FP16       | Slow            | Excellent  |
| INT8       | Medium          | Very Good  |
| INT4       | Fast            | Good  |
| GGUF q4_0  | Fastest (CPU)   | Acceptable  |

---

## Observations
- FP16 provides the highest output quality but has the largest memory footprint.
- INT8 offers the best balance between memory efficiency and quality.
- INT4 significantly reduces memory usage with a small degradation in output quality.
- GGUF enables efficient **CPU-only inference**, making the model deployable on edge devices.
- The latest llama.cpp CMake-based build was used, and quantisation was performed using the `llama-quantize` binary.

---

## Conclusion
Quantisation enables practical deployment of large language models by significantly reducing memory usage and improving inference speed.  
For GPU deployment, **INT8** provides the best quality–performance trade-off, while **INT4** and **GGUF (q4_0)** are ideal for constrained environments and CPU-based inference.

---

## Disclaimer
This model was fine-tuned on domain-specific data for educational and research purposes only and is **not intended for real-world medical or clinical use**.
