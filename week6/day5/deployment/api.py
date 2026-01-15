from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pydantic import BaseModel
import logging
import uuid
from monitoring.drift_checker import DriftChecker
import pandas as pd 


# Initializing FastAPI app
app = FastAPI()

# initializing a drift checker 

logging.basicConfig(filename='prediction_logs.csv', level=logging.INFO)

# Loading the trained model
MODEL_PATH = "./models/model.pkl"
model = joblib.load(MODEL_PATH)

# Initialize DriftChecker
drift_checker = DriftChecker(model_path=MODEL_PATH, baseline_data_path='./deployment/baseline_data.csv')  

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

        # Check for data drift
        drift_alert, drift_report = drift_checker.check_data_drift(pd.DataFrame(features, columns=['feature1', 'feature2']))

        # Log drift if detected
        drift_checker.log_drift(drift_alert, drift_report)

        # If no drift, make the prediction
        if not drift_alert:
            prediction = model.predict(features)
            # Log the prediction request and result
            log_prediction(request_id, features, prediction)
            return {"request_id": request_id, "prediction": prediction.tolist()}
        else:
            raise HTTPException(status_code=400, detail="Data drift detected. Model performance may be degraded.")

    except Exception as e:
        logging.error(f"Error in request {request_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
# Function to log prediction details
def log_prediction(request_id, features, prediction):
    logging.info(f"{request_id},{features[0][0]},{features[0][1]},{prediction[0]}")
