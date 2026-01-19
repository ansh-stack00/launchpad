import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

MODEL_PATH = Path("src/models/best_model.pkl")
X_TRAIN_PATH = Path("src/data/processed/X_train.csv")
OUTPUT_DIR = Path("src/evaluation/plots")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

X_train = pd.read_csv(X_TRAIN_PATH)

importances = model.feature_importances_
feature_names = X_train.columns

fi_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
}).sort_values(by="importance", ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(fi_df["feature"][:20][::-1], fi_df["importance"][:20][::-1])
plt.title("Top 20 Feature Importances (Random Forest)")
plt.xlabel("Importance")
plt.ylabel("Feature")

output_path = OUTPUT_DIR / "feature_importance.png"
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"Feature importance chart saved to {output_path}")

