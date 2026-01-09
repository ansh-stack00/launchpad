import json

INPUT_PATH = "data/raw/finance_raw.jsonl"
OUTPUT_TRAIN = "data/train.jsonl"
OUTPUT_VAL = "data/val.jsonl"

train_data = []
val_data = []

with open(INPUT_PATH, "r") as f:
    for line in f:

        # Strip  leading or trailing whitespace/newlines
        line = line.strip()  
        if not line: 
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Skipping invalid JSON line: {line}")
            print(f"Error details: {e}")
            continue  

        if not item.get("instruction") or not item.get("output"):
            continue 
        
        # Cleaning  up instruction, input, and output
        item["instruction"] = item["instruction"].strip()
        item["input"] = item.get("input", "").strip()
        item["output"] = item["output"].strip()

        train_data.append(item)

# splitting to 90/10 for test and validation 
split_idx = int(0.9 * len(train_data))
train, val = train_data[:split_idx], train_data[split_idx:]


with open(OUTPUT_TRAIN, "w") as f:
    for item in train:
        f.write(json.dumps(item) + "\n")

with open(OUTPUT_VAL, "w") as f:
    for item in val:
        f.write(json.dumps(item) + "\n")

print(f"Train samples: {len(train)}")
print(f"Validation samples: {len(val)}")
