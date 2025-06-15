import sqlite3

def init_db():
    print("📦 Initializing database...")

    conn = sqlite3.connect("booking.db")
    c = conn.cursor()

    # === Bookings Table ===
    c.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_reg TEXT UNIQUE,
            client_name TEXT,
            client_id TEXT,
            sale_date TEXT,
            status TEXT DEFAULT 'booked',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # === Payments Table ===
    c.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_reg TEXT,
            amount INTEGER,
            reference TEXT,
            date TEXT,
            FOREIGN KEY(vehicle_reg) REFERENCES bookings(vehicle_reg)
        )
    """)
        # === Users Table ===
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT CHECK(role IN ('admin', 'user')) NOT NULL
        )
    """)


    conn.commit()
    conn.close()
    print("✅ booking.db initialized.")
