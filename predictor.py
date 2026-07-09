import pandas as pd
import sqlite3
from sklearn.tree import DecisionTreeClassifier

# 1. Load your historical data
conn = sqlite3.connect("expenses.db")
df = pd.read_sql_query("SELECT * FROM tracker", conn)
conn.close()

# 2. Prepare Data (Features vs. Target)
# X (Input) = The amount spent. It must be a 2D array, hence double brackets.
# y (Output) = The category we want to predict.
X = df[["amount"]] 
y = df["category"] 

# 3. Initialize and Train the Model
model = DecisionTreeClassifier()
model.fit(X, y) # This is the actual "learning" phase

# 4. Make a Prediction
test_amount = 12.50
test_data = pd.DataFrame({"amount": [test_amount]})
prediction = model.predict(test_data)

print(f"An expense of ${test_amount} is predicted to be: {prediction[0]}")