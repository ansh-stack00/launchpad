import pickle
import pandas as pd
import shap
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

MODEL_PATH = Path("src/models/best_model.pkl")
X_TRAIN_PATH = Path("src/data/processed/X_train.csv")
OUTPUT_DIR = Path("src/evaluation/plots")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)




with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

X_train = pd.read_csv(X_TRAIN_PATH)
X_train = X_train.apply(pd.to_numeric, errors="coerce")
X_train = X_train.dropna(axis=1, how="all")
X_train = X_train.fillna(0)

if hasattr(model, "feature_names_in_"):
    X_train = X_train[model.feature_names_in_]
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)

if isinstance(shap_values, list):
    shap_vals = shap_values[1] 
elif isinstance(shap_values, np.ndarray) and shap_values.ndim == 3:
    shap_vals = shap_values[:, :, 1]
else:
    shap_vals = shap_values
assert shap_vals.shape[1] == X_train.shape[1], (
    f"SHAP shape {shap_vals.shape} != X shape {X_train.shape}"
)

plt.figure()
shap.summary_plot(
    shap_vals,
    X_train,
    show=False
)

output_path = OUTPUT_DIR / "shap_summary.png"
plt.savefig(output_path, bbox_inches="tight")
plt.close()

print(f"SHAP summary plot saved to {output_path}")


