import sqlite3
import random

# Connect to your existing database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Clear out your old manual entries to start fresh
cursor.execute("DELETE FROM tracker")

# Define the rules of our mock data
# Format: "Category": (Min Price, Max Price)
categories = {
    "food": (5, 50),
    "clothes": (30, 150),
    "electronics": (150, 800),
    "rent": (800, 2500)
}

print("Generating 1,000 mock records...")

# Generate 1,000 random rows
for _ in range(1000):
    category = random.choice(list(categories.keys()))
    min_price, max_price = categories[category]
    
    # Generate a random float between the min and max price, rounded to 2 decimals
    amount = round(random.uniform(min_price, max_price), 2)
    
    # Insert into the database
    cursor.execute("INSERT INTO tracker (date, category, amount) VALUES (?, ?, ?)", ("10/10/2026", category, amount))

conn.commit()
conn.close()

print("Database seeded successfully.")