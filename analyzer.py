import pandas as pd
import sqlite3

# 1. Connect to the SQLite database
conn = sqlite3.connect("expenses.db")

# 2. Run a SQL query directly into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM tracker", conn)

# 3. Calculate the grand total
total_spent = df["amount"].sum()
print(f"Total spent: {total_spent:.2f}")

# 4. Calculate the total per category
category_totals = df.groupby("category")["amount"].sum()
print("\n--- Spending by Category ---")
print(category_totals)

# Close the connection
conn.close()