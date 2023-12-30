import sqlite3
conn = sqlite3.connect('data11.db')
cursor = conn.cursor()
conn.execute("INSERT INTO student(emp_name, emp_id, emp_post, emp_phone) VALUES('karun', 005, 'Msc', 8963254107)")
conn.execute("INSERT INTO student(emp_name, emp_id, emp_post, emp_phone) VALUES('naren', 009, 'Bsc', 8596412370)")
conn.execute("INSERT INTO student(emp_name, emp_id, emp_post, emp_phone) VALUES('kisor', 001, 'BTech', 4562710390)")
conn.commit()
conn.close()
rows = conn.execute('SELECT * FROM student')
for row in rows:
    print(row)
print("\n Insert successfully")
