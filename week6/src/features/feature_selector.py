import numpy as np
import json
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path.cwd()

X_train = pd.read_csv(PROJECT_ROOT / "src/data/processed/X_features.csv")
y_train = pd.read_csv(PROJECT_ROOT / "src/data/processed/y.csv")

y_train = y_train.values.ravel()

X_train = X_train.select_dtypes(include=[np.number])
feature_names = X_train.columns.tolist()

mi_scores = mutual_info_classif(X_train, y_train, random_state=42)

mi_features = sorted(
    zip(feature_names, mi_scores),
    key=lambda x: x[1],
    reverse=True
)

TOP_K = 20
selected = mi_features[:TOP_K]

with open(PROJECT_ROOT / "src/features/selected_features.json", "w") as f:
    json.dump([f[0] for f in selected], f, indent=4)

features = [f[0] for f in selected]
scores = [f[1] for f in selected]

plt.figure(figsize=(10, 6))
plt.barh(features, scores)
plt.gca().invert_yaxis()
plt.title("Top Titanic Feature Importance (Mutual Info)")
plt.xlabel("MI Score")
plt.tight_layout()
plt.savefig(PROJECT_ROOT / "src/features/feature_importance.png")
plt.show()

print("Feature selection completed")
