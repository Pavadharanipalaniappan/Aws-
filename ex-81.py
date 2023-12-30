import sqlite3
conn=sqlite3.connect('data11.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE student1(emp_name char(20),emp_id number(5),emp_post char(30),emp_phone number(10))''')
print("\n Student  Table is created")