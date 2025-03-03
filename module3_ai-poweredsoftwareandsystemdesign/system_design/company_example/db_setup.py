# db_setup.py
import sqlite3
import random
import datetime
from database_connection import DatabaseConnection

def setup_database():
    # Establish a connection to SQLite
    conn = DatabaseConnection().connection
    cursor = DatabaseConnection().cursor

    # Create the Company table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Company (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL
    );
    ''')

    # Create the TimeSeries table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TimeSeries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER NOT NULL,
        value REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (company_id) REFERENCES Company(id)
    );
    ''')

    # Sample data for companies
    companies = [
        ("AAPL", "Apple Inc."),
        ("MSFT", "Microsoft Corporation"),
        ("GOOGL", "Alphabet Inc."),
        ("AMZN", "Amazon.com Inc."),
        ("TSLA", "Tesla Inc."),
        ("META", "Meta Platforms Inc."),
        ("NFLX", "Netflix Inc."),
        ("NVDA", "NVIDIA Corporation"),
        ("INTC", "Intel Corporation"),
        ("IBM", "International Business Machines Corporation")
    ]

    # Insert companies into the database
    cursor.executemany('''
    INSERT INTO Company (ticker, name) VALUES (?, ?)
    ON CONFLICT(ticker) DO NOTHING;
    ''', companies)

    # Retrieve company IDs
    cursor.execute("SELECT id, ticker FROM Company;")
    company_ids = {ticker: id for id, ticker in cursor.fetchall()}

    # Generate time-series data
    start_date = datetime.date(2023, 1, 1)
    n_days = 100

    data_entries = []
    for ticker, company_id in company_ids.items():
        for day_offset in range(n_days):
            date = start_date + datetime.timedelta(days=day_offset)
            value = round(random.uniform(100, 500), 2)  # Random stock value
            data_entries.append((company_id, value, date.strftime("%Y-%m-%d")))

    cursor.executemany('''
    INSERT INTO TimeSeries (company_id, value, date) VALUES (?, ?, ?);
    ''', data_entries)

    # Commit and close the connection
    conn.commit()
    print("Database setup complete with sample data.")

if __name__ == "__main__":
    setup_database()
