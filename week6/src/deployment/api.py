from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, create_model
import pandas as pd
import pickle
import uuid
from pathlib import Path
from datetime import datetime
import json

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODELS_DIR = PROJECT_ROOT / "src" / "models"
LOGS_FILE = PROJECT_ROOT / "src" / "prediction" / "prediction_logs.csv"
FEATURES_FILE = PROJECT_ROOT / "src/features/selected_features.json"

app = FastAPI(title="Titanic Survival Predictor API")

model_path = MODELS_DIR / "best_model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(FEATURES_FILE, "r") as f:
    selected_features = json.load(f)

# Dynamically create Pydantic model based on selected features
fields = {feat: (float if "Age" in feat or "Fare" in feat else int, ...) for feat in selected_features}
PredictionInput = create_model("PredictionInput", **fields)


@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        data = pd.DataFrame([input_data.dict()])

        # Ensure column order matches training
        missing_cols = set(selected_features) - set(data.columns)
        for col in missing_cols:
            data[col] = 0  # fill missing features with 0

        data = data[selected_features]

        pred_proba = model.predict_proba(data)[:, 1][0]
        pred_class = int(pred_proba >= 0.5)

        log_entry = {
            "request_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "input": input_data.dict(),
            "pred_class": pred_class,
            "pred_proba": float(pred_proba)
        }

        log_df = pd.DataFrame([log_entry])
        if LOGS_FILE.exists():
            log_df.to_csv(LOGS_FILE, mode="a", header=False, index=False)
        else:
            log_df.to_csv(LOGS_FILE, index=False)

        return {
            "request_id": log_entry["request_id"],
            "prediction": pred_class,
            "probability": pred_proba,
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
