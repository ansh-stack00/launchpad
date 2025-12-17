import numpy as np
import json
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# importing ml models 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

# selecting models
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
# path setup 
PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_DIR = PROJECT_ROOT / "src" / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "src" / "models"
EVAL_DIR = PROJECT_ROOT / "src" / "evaluation"

MODELS_DIR.mkdir(parents=True, exist_ok=True)
EVAL_DIR.mkdir(parents=True, exist_ok=True)

# loading data 
X_train = np.load(PROCESSED_DIR / "X_train.npy")
X_test = np.load(PROCESSED_DIR / "X_test.npy")
y_train = np.load(PROCESSED_DIR / "y_train.npy")
y_test = np.load(PROCESSED_DIR / "y_test.npy")

print("Data loaded successfully")

# defining models 
models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        eval_metric="logloss",
        random_state=42
    ),

    "Neural Network": MLPClassifier(
        hidden_layer_sizes=(64, 32),
        max_iter=500,
        random_state=42
    )
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

results = {}

for model_name, model in models.items():
    print(f"\n🔹 Training {model_name}")

    # Cross-validation accuracy
    cv_scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="accuracy"
    )

    print(f"CV Accuracy: {cv_scores.mean():.4f}")

    # Train model on full training data
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Probabilities (needed for ROC-AUC)
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)[:, 1]
        roc_auc = roc_auc_score(y_test, y_proba)
    else:
        roc_auc = None

    # Metrics
    results[model_name] = {
        "CV_Accuracy": cv_scores.mean(),
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1_Score": f1_score(y_test, y_pred),
        "ROC_AUC": roc_auc
    }

# selecting best models on the basis of f1 score 
best_model_name = max(results, key=lambda x: results[x]["F1_Score"])
best_model = models[best_model_name]

print(f"\nBest Model: {best_model_name}")

# saving the best model
with open(MODELS_DIR / "best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("Best model saved")

with open(EVAL_DIR / "metrics.json", "w") as f:
    json.dump(results, f, indent=4)

print("Metrics saved")

y_best_pred = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_best_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title(f"Confusion Matrix - {best_model_name}")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig(EVAL_DIR / "confusion_matrix.png")
plt.show()

print("Confusion matrix generated")

print("\nDAY 3 TRAINING PIPELINE COMPLETED SUCCESSFULLY")
