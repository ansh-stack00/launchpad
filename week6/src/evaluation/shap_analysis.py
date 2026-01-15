import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "src" / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "src" / "models"
EVAL_DIR = PROJECT_ROOT / "src" / "evaluation"

EVAL_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    X = pd.read_csv(DATA_DIR / "X_features.csv")
    y = pd.read_csv(DATA_DIR / "y.csv").values.ravel()
    X = X.select_dtypes(include=[np.number])
    return X, y

def train_or_load_model(X_train, y_train):
    model_file = MODELS_DIR / "best_model.pkl"
    if model_file.exists():
        with open(model_file, "rb") as f:
            model = pickle.load(f)
        print("Model loaded from disk")
    else:
        model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
        model.fit(X_train, y_train)
        with open(model_file, "wb") as f:
            pickle.dump(model, f)
        print("Model trained and saved")
    return model

def explain_model_with_shap(model, X_train, save_path=None):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)
    
    plt.figure()
    shap.summary_plot(shap_values, X_train, show=False)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"SHAP summary plot saved to {save_path}")
    plt.show()
    return shap_values

def plot_feature_importance(model, X_train, save_path=None):
    feature_importance = model.feature_importances_
    sorted_idx = feature_importance.argsort()
    plt.figure(figsize=(10, 6))
    plt.barh(X_train.columns[sorted_idx], feature_importance[sorted_idx])
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance from the Model')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Feature importance plot saved to {save_path}")
    plt.show()

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X.values, y, test_size=0.2, stratify=y, random_state=42
    )
    X_train_df = pd.DataFrame(X_train, columns=X.columns)

    model = train_or_load_model(X_train_df, y_train)
    
    shap_values = explain_model_with_shap(
        model,
        X_train_df,
        save_path=EVAL_DIR / "shap_summary.png"
    )
    
    plot_feature_importance(
        model,
        X_train_df,
        save_path=EVAL_DIR / "feature_importance.png"
    )
