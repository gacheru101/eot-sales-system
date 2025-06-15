import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("booking.db")
c = conn.cursor()

username = "admin"
password = "admin123"
role = "admin"

hashed_pw = generate_password_hash(password)

c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
          (username, hashed_pw, role))

conn.commit()
conn.close()

print("✅ Admin user created: username=admin, password=admin123")
