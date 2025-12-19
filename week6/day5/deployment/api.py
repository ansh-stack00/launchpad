from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pydantic import BaseModel
import logging
import uuid


app = FastAPI()


logging.basicConfig(filename='prediction_logs.csv', level=logging.INFO)

# Loading the model
MODEL_PATH = "models/model.pkl"
model = joblib.load(MODEL_PATH)

# Define the input schema using Pydantic
class PredictionRequest(BaseModel):
    feature1: float
    feature2: float

# Prediction endpoint
@app.post("/predict")
async def predict(request: PredictionRequest):
    request_id = str(uuid.uuid4())  # Generate unique request ID
    try:
        features = np.array([[request.feature1, request.feature2]])
        prediction = model.predict(features)

        # Log the prediction request and result
        log_prediction(request_id, features, prediction)

        return {"request_id": request_id, "prediction": prediction.tolist()}

    except Exception as e:
        logging.error(f"Error in request {request_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Function to log prediction details
def log_prediction(request_id, features, prediction):
    logging.info(f"{request_id},{features[0][0]},{features[0][1]},{prediction[0]}")
