from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# --- 1. PASTE YOUR CONNECTION STRING HERE ---
DATABASE_URL = "postgresql://postgres:[YOUR-PASSWORD]@your-supabase-url.pooler.supabase.com:6543/postgres"

# --- 2. DATABASE SETUP ---
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ExpenseLog(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    predicted_category = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create the table in Supabase automatically if it doesn't exist
Base.metadata.create_all(bind=engine)

# --- 3. FASTAPI SETUP ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model (Keep your existing model loading code here)
model = joblib.load("expense_model.pkl")

# --- 4. PREDICT AND SAVE TO DATABASE ---
@app.get("/predict")
def predict(amount: float):
    # 1. Make the prediction (Keep your existing prediction logic)
    df = pd.DataFrame({"amount": [amount]})
    prediction = model.predict(df)
    category = prediction[0]

    # 2. Save to Supabase
    db = SessionLocal()
    new_expense = ExpenseLog(amount=amount, predicted_category=category)
    db.add(new_expense)
    db.commit()
    db.close()

    return {"amount": amount, "predicted_category": category}