import torch
from transformers import AutoModelForCausalLM, AutoTokenizer,BitsAndBytesConfig
from peft import PeftModel

BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
LORA_PATH = "./lora-output"
OUTPUT_DIR = "./merged/merged_model"

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.float16,
    device_map="auto"
)

model = PeftModel.from_pretrained(base_model, LORA_PATH)

print("Merging LoRA adapters...")
model = model.merge_and_unload()

model.save_pretrained(OUTPUT_DIR, safe_serialization=True)
tokenizer.save_pretrained(OUTPUT_DIR)

print("LoRA merged and saved")



bnb_int8 = BitsAndBytesConfig(load_in_8bit=True)

model = AutoModelForCausalLM.from_pretrained(
    "./merged/merged_model",
    quantization_config=bnb_int8,
    device_map="auto"
)

model.save_pretrained("./quantized/int8", safe_serialization=True)

print("INT8 model saved")





bnb_int4 = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    "./merged/merged_model",
    quantization_config=bnb_int4,
    device_map="auto"
)

model.save_pretrained("./quantized/int4", safe_serialization=True)

print("INT4 model saved")
