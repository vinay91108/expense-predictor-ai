from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pre-trained model directly from the hard drive
model = joblib.load("expense_model.pkl")

@app.get("/predict")
def predict_category(amount: float):
    test_data = pd.DataFrame({"amount": [amount]})
    prediction = model.predict(test_data)
    
    return {"amount": amount, "predicted_category": prediction[0]}