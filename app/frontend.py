from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import pandas as pd
import pickle

# ✅ Try loading the model
try:
    with open('model (6).pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print("❌ Model file not found: 'model (6).pkl'")

# ✅ Create FastAPI instance
app = FastAPI()

# ✅ Input model for crop prediction
class CropInput(BaseModel):
    Temperature: Annotated[float, Field(..., gt=0, lt=100, description="Temperature in Celsius")]
    Humidity: Annotated[float, Field(..., description='Humidity in Percentage')]
    Rainfall: Annotated[float, Field(..., description='Rainfall in mm')]
    PH: Annotated[float, Field(..., description='Soil pH')]
    Nitrogen: Annotated[float, Field(..., description='Nitrogen in kg/ha')]
    Phosphorous: Annotated[float, Field(..., description='Phosphorous in kg/ha')]
    Potassium: Annotated[float, Field(..., description='Potassium in kg/ha')]
    Carbon: Annotated[float, Field(..., description='Carbon in kg/ha')]
    Acidic_Soil: Annotated[Literal[0, 1], Field(..., description='0 = No, 1 = Yes')]
    Alkaline_Soil: Annotated[Literal[0, 1], Field(..., description='0 = No, 1 = Yes')]
    Loamy_Soil: Annotated[Literal[0, 1], Field(..., description='0 = No, 1 = Yes')]
    Neutral_Soil: Annotated[Literal[0, 1], Field(..., description='0 = No, 1 = Yes')]
    Peaty_Soil: Annotated[Literal[0, 1], Field(..., description='0 = No, 1 = Yes')]

# ✅ Home route
@app.get("/")
def home():
    return {"message": "Welcome to Crop Prediction API"}

# ✅ Prediction route
@app.post("/predict")
def predict_crop(data: CropInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Convert input data to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make prediction
    try:
        prediction = model.predict(input_df)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

    return {"predicted_crop": prediction}
