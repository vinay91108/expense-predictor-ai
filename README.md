# Expense Predictor AI

A full-stack application that uses a machine learning model to predict expense categories based on the amount entered, 
with a secure backend to log your data.

## Features
- **AI Prediction:** Uses a machine learning model to categorize expenses.
- **Secure Logging:** Automatically saves all predictions to a Supabase PostgreSQL database.
- **RESTful API:** Built with FastAPI, featuring Swagger UI for easy testing and integration.
- **Production Ready:** Hosted on Render with secure environment variable management.

## API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/predict` | Predicts category based on amount and saves to DB. |
| `POST` | `/save_expense` | Manually save an expense to the database. |

## Deployment Setup
This project uses secure environment variables for database connectivity.
Ensure your `DATABASE_URL` is configured in your production environment 
settings (e.g., Render/Heroku) rather than hardcoding it in the script.
