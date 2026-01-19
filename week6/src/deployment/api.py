import uuid
import pickle
import pandas as pd
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime

MODEL_DIR = Path("src/models")
LOG_PATH = Path("src/prediction_logs.csv")

app = FastAPI(title="Titanic Survival API")
MODEL_PATH = MODEL_DIR / "best_model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

FEATURE_NAMES = model.feature_names_in_.tolist()


class InputSchema(BaseModel):
    Sex: int = Field(..., example=1, description="0 = male, 1 = female")
    Age: float = Field(..., example=29)
    Parch: int = Field(..., example=0)
    Fare: float = Field(..., example=71.2)
    IsAlone: int = Field(..., example=0)
    FarePerPerson: float = Field(..., example=35.6)
    Title_Dr: int = Field(0, example=0)
    Title_Mr: int = Field(1, example=1)
    Title_Mrs: int = Field(0, example=0)


@app.post("/predict")
def predict(payload: InputSchema):
    request_id = str(uuid.uuid4())

    X = pd.DataFrame([payload.dict()])

    X = X.reindex(columns=FEATURE_NAMES, fill_value=0)
    proba = model.predict_proba(X)[0, 1]
    prediction = int(proba >= 0.5)

    log_row = {
        "timestamp": datetime.utcnow().isoformat(),
        "request_id": request_id,
        "prediction": prediction,
        "probability": proba,
        **payload.dict()
    }

    log_df = pd.DataFrame([log_row])

    if LOG_PATH.exists():
        log_df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        log_df.to_csv(LOG_PATH, index=False)

    return {
        "request_id": request_id,
        "prediction": prediction,
        "probability": proba
    }
