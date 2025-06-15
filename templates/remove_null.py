import sqlite3

conn = sqlite3.connect("booking.db")
c = conn.cursor()

# Delete any booking for GKB 018M that has no price
c.execute("DELETE FROM bookings WHERE vehicle_reg = 'GKB 018M' AND price IS NULL")

conn.commit()
conn.close()

print("✅ Removed invalid booking entry for GKB 018M with missing price.")
