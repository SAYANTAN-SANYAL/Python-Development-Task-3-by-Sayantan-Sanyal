import sqlite3


conn = sqlite3.connect('student.db')
c = conn.cursor()
c.execute("""CREATE TABLE students_details(
                 stud_ID INTEGER PRIMARY KEY,
                 username VARCHAR(20),
                 password VARCHAR(20),
                 name VARCHAR(20),
                 branch VARCHAR(20),
                 regd_no INTEGER,
                 marks INTEGER);
                 """)
c.execute("""INSERT INTO students_details(username,password) 
             VALUES("Sayantan","Santu")
             """)



conn.commit()
conn.close()