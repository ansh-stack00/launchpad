import joblib
import numpy as np
from sklearn.linear_model import LinearRegression


X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([3, 7, 11, 15])

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)


model_path = "./models/model.pkl"
joblib.dump(model, model_path)

print(f"Model saved to {model_path}")
