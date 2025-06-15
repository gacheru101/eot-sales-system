# create_user.py
import sqlite3
from werkzeug.security import generate_password_hash

def add_user(username, password, role="user"):
    conn = sqlite3.connect("booking.db")
    c = conn.cursor()

    hashed_password = generate_password_hash(password)
    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
        conn.commit()
        print(f"✅ User '{username}' added successfully with role '{role}'")
    except sqlite3.IntegrityError:
        print("❌ Username already exists!")
    finally:
        conn.close()

# Add users
add_user("admin", "admin123", role="admin")
add_user("james", "password123", role="user")
