import json
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score
import pandas as pd 

TUNING_RESULTS_PATH = Path("src/tuning/results.json")
MODEL_PATH = Path("src/models/best_model.pkl")


def tune_rf():
    X_train=pd.read_csv("src/data/processed/X_train.csv")
    X_test=pd.read_csv("src/data/processed/X_test.csv")
    y_train=pd.read_csv("src/data/processed/y_train.csv")
    y_test=pd.read_csv("src/data/processed/y_test.csv")

    rf = RandomForestClassifier(
        random_state=42,
    )

    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [4,6,8],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2,]
    }

    grid = GridSearchCV(
        rf,
        param_grid=param_grid,
        scoring="roc_auc",
        cv=5,
        n_jobs=-1,
    )

    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_

# Evaluatin on test data
    y_proba = best_model.predict_proba(X_test)[:, 1]
    test_roc_auc = roc_auc_score(y_test, y_proba)
    results = {
        "best_params": grid.best_params_,
        "cv_best_roc_auc": grid.best_score_,
        "test_roc_auc": test_roc_auc
    }

    with open(TUNING_RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=4)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(best_model, f)
    print("Random forest tuning completed")
    print(results)



if __name__ == "__main__":
    tune_rf()
