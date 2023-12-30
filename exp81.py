import sqlite3
db_file = "student.db"
connection = sqlite3.connect(db_file)
cursor = connection.cursor()
cmd="""CREATE TABLE Student_detail(name varchar,rollno varchar,dob date,dep varchar,year number)"""
cursor.execute(cmd)
connection.commit()
cursor.close()
connection.close()
print("Table 'student.db' created successfully in", db_file)