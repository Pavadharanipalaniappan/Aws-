import sqlite3
conn = sqlite3.connect('data11.db')
cursor = conn.cursor()
print("Before Updating\n")
rows = conn.execute('SELECT * FROM student')
for row in rows:
    print(row)
cursor.execute("UPDATE student SET emp_post='MBA', emp_phone=8563240710 WHERE emp_id=001")
print("\nAfter Updating\n")
rows = conn.execute('SELECT * FROM student')
for row in rows:
    print(row)
conn.commit()
conn.close()