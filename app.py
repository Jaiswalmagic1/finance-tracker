from flask import Flask, render_template
import sqlite3

import os

# Ensure database exists when app starts
if not os.path.exists("expenses.db"):
    import init_db

app = Flask(__name__)

@app.route("/")
def home():
    # Connect to DB and fetch summary
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    data = cur.fetchall()
    conn.close()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
