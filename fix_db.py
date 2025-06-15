import sqlite3
conn = sqlite3.connect("booking.db")
c = conn.cursor()

c.execute("SELECT vehicle_reg, price FROM bookings WHERE UPPER(vehicle_reg) = 'GKB 006M'")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
