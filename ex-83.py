import sqlite3
conn = sqlite3.connect('data11.db')
cursor = conn.cursor()
rows = conn.execute('SELECT * FROM student')
for row in rows:
    print(row)
conn.close()