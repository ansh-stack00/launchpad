import json
import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "src" / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "src" / "models"
TUNING_DIR = PROJECT_ROOT / "src" / "tuning"

MODELS_DIR.mkdir(parents=True, exist_ok=True)
TUNING_DIR.mkdir(parents=True, exist_ok=True)

def grid_search_tuning():
    X = pd.read_csv(DATA_DIR / "X_features.csv")
    y = pd.read_csv(DATA_DIR / "y.csv").values.ravel()

    X = X.select_dtypes(include=[np.number])

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X.values,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    param_grid = {
        "n_estimators": [50, 100, 150],
        "max_depth": [10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    model = RandomForestClassifier(random_state=42)

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=5,
        scoring="roc_auc",
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    y_proba = best_model.predict_proba(X_test)[:, 1]
    roc_auc = roc_auc_score(y_test, y_proba)

    results = {
        "best_params": grid_search.best_params_,
        "cv_best_score": grid_search.best_score_,
        "test_roc_auc": roc_auc
    }

    with open(TUNING_DIR / "results.json", "w") as f:
        json.dump(results, f, indent=4)

    with open(MODELS_DIR / "best_model.pkl", "wb") as f:
        pickle.dump(best_model, f)

    print("Best Parameters:", grid_search.best_params_)
    print(f"Test ROC-AUC: {roc_auc:.4f}")
    print("Tuning results and model saved")

    return best_model, results

if __name__ == "__main__":
    grid_search_tuning()
