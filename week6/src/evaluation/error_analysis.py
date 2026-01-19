import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import confusion_matrix

MODEL_PATH = Path("src/models/best_model.pkl")
X_TEST_PATH = Path("src/data/processed/X_test.csv")
Y_TEST_PATH = Path("src/data/processed/y_test.csv")
OUTPUT_DIR = Path("src/evaluation/plots")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

X_test = pd.read_csv(X_TEST_PATH)
y_test = pd.read_csv(Y_TEST_PATH)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Pred 0", "Pred 1"],
    yticklabels=["True 0", "True 1"]
)
plt.title("Confusion Matrix Heatmap")
plt.xlabel("Predicted")
plt.ylabel("Actual")

output_path = OUTPUT_DIR / "error_heatmap.png"
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"Error analysis heatmap saved to {output_path}")
