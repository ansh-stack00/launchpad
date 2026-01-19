import json
import pickle
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

MODEL_PATH = Path("src/models/best_model.pkl")
METRICS_PATH = Path("src/evaluation/metrics.json")


def evaluate_model(model, X, y):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    metrics = {
        "accuracy": [],
        "precision": [],
        "recall": [],
        "f1": [],
        "roc_auc": []
    }



    for train_idx, val_idx in skf.split(X, y):
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        model.fit(X_train, y_train)
        preds = model.predict(X_val)
        probs = model.predict_proba(X_val)[:, 1]
        metrics["accuracy"].append(accuracy_score(y_val, preds))
        metrics["precision"].append(precision_score(y_val, preds))
        metrics["recall"].append(recall_score(y_val, preds))
        metrics["f1"].append(f1_score(y_val, preds))
        metrics["roc_auc"].append(roc_auc_score(y_val, probs))

    return {k: np.mean(v) for k, v in metrics.items()}


def train_models():
    X_train=pd.read_csv("src/data/processed/X_train.csv")
    X_test=pd.read_csv("src/data/processed/X_test.csv")
    y_train=pd.read_csv("src/data/processed/y_train.csv")
    y_test=pd.read_csv("src/data/processed/y_test.csv")
    models = {
        "LogisticRegression": LogisticRegression(
            max_iter=1000, 
            penalty="l2"
        ),
        "RandomForest": RandomForestClassifier(
            n_estimators=200, 
            max_depth=None, 
            random_state=42
        ),
        "XGBoost": XGBClassifier(
            eval_metric="logloss", 
            use_label_encoder=False
        ),
        "NeuralNetwork": MLPClassifier(
            hidden_layer_sizes=(64, 32),
            max_iter=500,
            random_state=42
        )
    }


    all_metrics = {}
    best_model = None
    best_score = 0
    for name, model in models.items():
        print(f"\nTraining {name}...")
        scores = evaluate_model(model, X_train, y_train)
        all_metrics[name] = scores
        print(f"{name} ROC-AUC: {scores['roc_auc']:.4f}")

        if scores["roc_auc"] > best_score:
            best_score = scores["roc_auc"]
            best_model = model

# Train best model on full training data
    best_model.fit(X_train, y_train)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(best_model, f)

    with open(METRICS_PATH, "w") as f:
        json.dump(all_metrics, f, indent=4)

    print("\nBest model saved")
    print("Metrics saved")

    y_pred = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig("src/evaluation/confusion_matrix.png", bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    train_models()
