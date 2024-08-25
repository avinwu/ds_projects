from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from typing import List, Optional


# Define a data model for a single house's features
class HouseFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: Optional[float]  # Handle possible null values
    population: float
    households: float
    median_income: float
    ocean_proximity: str


# Define the input model to accept a list of HouseFeatures
class HouseData(BaseModel):
    features: List[HouseFeatures]


# Load the model
model = joblib.load('regressor.pkl')

# Create FastAPI instance
app = FastAPI()


# Define the prediction endpoint
@app.post("/predict")
def predict_price(data: List[HouseFeatures]):
    # Convert the list of HouseFeatures to a DataFrame
    df_input = pd.DataFrame([feature.dict() for feature in data])

    # Make predictions
    prediction = model.predict(df_input).round()

    # Return predictions as a list
    return {"predicted_price": prediction.tolist()}

# FastAPI command to run
# uvicorn app:app --reload
