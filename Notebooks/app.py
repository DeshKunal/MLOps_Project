from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import numpy as np

# Initialize FastAPI app
app = FastAPI(
    title="German Credit Model API",
    description="API for predicting credit risk",
    version="1.0.0"
)

# Define the expected input schema using Pydantic
class InputData(BaseModel):
    ExistingAccount_Status: str
    Duration_Months: int
    Credit_History: str
    Purpose: str
    Credit_Amount: float
    SavingsAccount_Bonds: str
    Present_Employment_Since: str
    Installment_Rate: int
    PersonalStatus_Sex: str
    OtherDebtors_Guarantors: str
    Present_Residence_Since: int
    Property: str
    Age_Years: int
    Other_Installment_Plans: str
    Housing: str
    Num_Existing_Credits: int
    Job: str
    Num_People_Liable: int
    Telephone: str
    Foreign_Worker: str

# Load the best model directly from MLflow artifact location
model_path = "C:/Users/kunal/Downloads/MLOps/Project/Gr-05_MLOps_Project/mlruns/540899927217565002/5ffe5026e5ef47efa4269d28d2d86080/artifacts/model"
try:
    model = mlflow.pyfunc.load_model(model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load the model: {e}")

@app.post("/predict", summary="Get Prediction", response_description="Prediction Result")
def predict(input_data: InputData):
    """
    Accepts a JSON object containing input features,
    converts it to a DataFrame, and returns the model prediction.
    """
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data.dict()])
        
        # Make prediction
        prediction = model.predict(input_df)
        
        # Convert numpy types to native Python types for JSON serialization
        if isinstance(prediction, np.ndarray):
            prediction = prediction.tolist()
        elif isinstance(prediction, (np.float64, np.int64)):
            prediction = prediction.item()
        
        return {"prediction": prediction}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


