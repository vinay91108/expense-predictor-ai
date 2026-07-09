from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# 1. Load Environment Variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Database Setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ExpenseLog(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    predicted_category = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# 3. FastAPI Setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("expense_model.pkl")

# Pydantic model for input
class Expense(BaseModel):
    amount: float
    category: str

# 4. Endpoints
@app.get("/predict")
def predict(amount: float):
    df = pd.DataFrame({"amount": [amount]})
    prediction = model.predict(df)
    category = prediction[0]

    # Save to Supabase
    db = SessionLocal()
    new_expense = ExpenseLog(amount=amount, predicted_category=category)
    db.add(new_expense)
    db.commit()
    db.close()

    return {"amount": amount, "predicted_category": category}

@app.post("/save_expense")
def save_expense(expense: Expense):
    db = SessionLocal()
    new_expense = ExpenseLog(amount=expense.amount, predicted_category=expense.category)
    db.add(new_expense)
    db.commit()
    db.close()
    return {"message": "Saved successfully!"}