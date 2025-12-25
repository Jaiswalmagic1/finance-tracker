import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

# Create the transactions table
cur.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL
)
""")

# Insert some sample data
cur.execute("INSERT INTO transactions (category, amount) VALUES (?, ?)", ("Food", 1200))
cur.execute("INSERT INTO transactions (category, amount) VALUES (?, ?)", ("Transport", 600))
cur.execute("INSERT INTO transactions (category, amount) VALUES (?, ?)", ("Shopping", 2500))

conn.commit()
conn.close()

print("Database initialized with sample data.")
