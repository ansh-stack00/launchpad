from fastapi import FastAPI, HTTPException
from pydantic import create_model
import pandas as pd
import pickle
import uuid
from pathlib import Path
from datetime import datetime
import json

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODELS_DIR = PROJECT_ROOT / "src" / "models"
FEATURES_FILE = PROJECT_ROOT / "src" / "features" / "selected_features.json"
LOGS_FILE = PROJECT_ROOT / "src" / "prediction" / "prediction_logs.csv"

app = FastAPI(title="Titanic Survival Predictor API")

with open(MODELS_DIR / "best_model.pkl", "rb") as f:
    model = pickle.load(f)

with open(FEATURES_FILE, "r") as f:
    selected_features = json.load(f)
PredictionInput = create_model(
    "PredictionInput",
    **{feat: (float, ...) for feat in selected_features}
)

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        X = pd.DataFrame([input_data.dict()])
        X = X[selected_features]  # enforce order

        pred_proba = model.predict_proba(X)[0, 1]
        pred_class = int(pred_proba >= 0.5)

        response = {
            "request_id": str(uuid.uuid4()),
            "prediction": pred_class,
            "probability": float(pred_proba),
            "timestamp": datetime.now().isoformat()
        }

        pd.DataFrame([{**input_data.dict(), **response}]).to_csv(
            LOGS_FILE,
            mode="a",
            header=not LOGS_FILE.exists(),
            index=False
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
