import pandas as pd
import numpy as np
import json
from scipy.stats import ks_2samp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "src" / "data" / "processed"
FEATURES_DIR = ROOT / "features"
LOGS_FILE = ROOT / "prediction"/"prediction_logs.csv"

X_train = np.load(DATA_DIR / "X_train.npy")

with open(FEATURES_DIR / "selected_features.json", "r") as f:
    feature_names = json.load(f)

X_train_df = pd.DataFrame(X_train, columns=feature_names)

if not LOGS_FILE.exists():
    print("No prediction logs found")
    exit()

logs = pd.read_csv(LOGS_FILE)

new_data = pd.json_normalize(logs["input"].apply(eval))
new_data = new_data[feature_names] 

drift_results = {}

for feature in feature_names:
    stat, p_value = ks_2samp(
        X_train_df[feature],
        new_data[feature]
    )
    drift_results[feature] = {
        "ks_stat": round(stat, 4),
        "p_value": round(p_value, 6),
        "drift_detected": p_value < 0.05
    }
print("\nDATA DRIFT REPORT")
print("=" * 40)

for feature, result in drift_results.items():
    status = "DRIFT" if result["drift_detected"] else "OK"
    print(f"{feature:20s} | {status} | p={result['p_value']}")

