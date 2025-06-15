import sqlite3

conn = sqlite3.connect("booking.db")
c = conn.cursor()

c.execute("SELECT vehicle_reg, price FROM bookings WHERE vehicle_reg = 'GKB 018M'")
print(c.fetchone())

conn.close()
