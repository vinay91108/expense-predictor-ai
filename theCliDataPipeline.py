import sqlite3

# 1. Connect to the database (creates 'expenses.db' automatically if it doesn't exist)
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# 2. Define the schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        category TEXT,
        amount REAL
    )
''')

# 3. Collect user input
date = input("enter the date: ")
category = input("enter the category: ")
amount = float(input("enter the amount: "))

# 4. Insert the data securely
cursor.execute("INSERT INTO tracker (date, category, amount) VALUES (?, ?, ?)", (date, category, amount))

# 5. Commit the transaction and close the connection
conn.commit()
conn.close()

print("Expense saved to SQLite database.")