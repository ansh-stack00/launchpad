from datasets import load_dataset
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def get_resoning_data():
    dataset = load_dataset(
        "FreedomIntelligence/medical-o1-reasoning-SFT",
        "en",
        split="train[:600]"
    )

    print(dataset[0])
    print(f"\nDataset size: {len(dataset)}")

    dataset.to_csv(RAW_DIR / "medical_reasoning.csv", index=False)

# if __name__ == "__main__":
#     get_resoning_data()