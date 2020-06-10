from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Login Window")
conn = sqlite3.connect('student.db')
c = conn.cursor()

def alter():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("""ALTER TABLE students_details
                 ADD COLUMN maths_marks INTEGER;
                 """)
    c.execute("""ALTER TABLE students_details
                 ADD COLUMN chemistry_marks INTEGER;
                 """)
    c.execute("""ALTER TABLE students_details
                ADD COLUMN biology_marks INTEGER;
                 """)
    conn.commit()
    conn.close()

def submit_1():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    mark_1 = math_mark.get()
    c.execute("""UPDATE students_details
                 SET maths_marks = '%s'
                 WHERE stud_ID = 1""" %(mark_1))
    conn.commit()
    conn.close()

def submit_2():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    mark_2 = chemistry_mark.get()
    c.execute("""UPDATE students_details
                 SET chemistry_marks = '%s'
                 WHERE stud_ID = 1""" %(mark_2))
    conn.commit()
    conn.close()

def submit_3():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    mark_3 = bio_mark.get()
    c.execute("""UPDATE students_details
                 SET biology_marks = '%s'
                 WHERE stud_ID = 1""" %(mark_3))
    conn.commit()
    conn.close()

def click_4():
    global bio_mark
    global button_9
    top_4 = Toplevel()
    top_4.title("Marks")
    bio_mark = Entry(top_4, textvariable=IntVar(), width=50)
    bio_mark.grid(row=0, column=1)
    bio_mark_label = Label(top_4, text="Mark")
    bio_mark_label.grid(row=0, column=0)
    button_9 = Button(top_4, text="Submit Biology marks", command=submit_3)
    button_9.grid(row=1, column=0, columnspan=2)
    z = bio_mark.get()
    return z

def click_3():
    global chemistry_mark
    global button_8
    top_3 = Toplevel()
    top_3.title("Marks")
    chemistry_mark = Entry(top_3, textvariable=IntVar(), width=50)
    chemistry_mark.grid(row=0, column=1)
    chemistry_mark_label = Label(top_3, text="Mark")
    chemistry_mark_label.grid(row=0, column=0)
    button_8 = Button(top_3, text="Submit Chemistry marks", command=submit_2)
    button_8.grid(row=1, column=0, columnspan=2)
    y = chemistry_mark.get()
    return y

def click_2():
    global math_mark
    global button_7
    top_2 = Toplevel()
    top_2.title("Marks")
    math_mark = Entry(top_2, textvariable=IntVar(), width=50)
    math_mark.grid(row=0, column=1)
    math_mark_label = Label(top_2, text="Mark")
    math_mark_label.grid(row=0, column=0)
    button_7 = Button(top_2, text="Submit Maths marks", command=submit_1)
    button_7.grid(row=1, column=0, columnspan=2)
    x = math_mark.get()
    return x

math_marks = click_2()
chem_marks = click_3()
bio_marks = click_4()

def cal_1():
    global cgpa
    sum_mark = math_marks + chem_marks + bio_marks
    cgpa = int(sum_mark) / 30
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("""UPDATE students_details
                 SET Cgpa = '%s'
                 WHERE stud_ID = 1""" %(cgpa))
    conn.commit()
    conn.close()
    return cgpa

cgpa_stud = cal_1()

def cal_2():
    global grade
    if (cgpa_stud == 10):
        grade = "O"
    elif ((cgpa_stud >= 9) & (cgpa_stud < 10)):
        grade = "E"
    elif ((cgpa_stud >= 8) & (cgpa_stud < 9)):
        grade = "A"
    elif ((cgpa_stud >= 7) & (cgpa_stud < 8)):
        grade = "B"
    elif ((cgpa_stud >= 6) & (cgpa_stud < 7)):
        grade = "C"
    elif ((cgpa_stud >= 5) & (cgpa_stud < 6)):
        grade = "D"
    elif (cgpa_stud < 5):
        grade = "F"
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("""UPDATE students_details
                 SET Grade = '%s'
                 WHERE stud_ID = 1""" % (grade))
    conn.commit()
    conn.close()
    return grade

def alter_1():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("""ALTER TABLE students_details
                 ADD COLUMN Cgpa INTEGER;
                 """)
    c.execute("""ALTER TABLE students_details
                 ADD COLUMN Grade VARCHAR(10);
                 """)
    conn.commit()
    conn.close()

def click_5():
    global button_10
    global cgpa_btn
    global grade_btn
    global new_input_btn
    global close_btn
    top_5 = Toplevel()
    top_5.title("GUI 3")
    button_10 = Button(top_5, text="Alter Table", command=alter_1)
    button_10.grid(row=0, column=0, columnspan=2)
    cgpa_btn = Button(top_5, text="CGPA", command=cal_1)
    cgpa_btn.grid(row=1, column=0, columnspan=2)
    grade_btn = Button(top_5, text="GRADE", command=cal_2)
    grade_btn.grid(row=2, column=0, columnspan=2)
    new_input_btn = Button(top_5, text="New Input", command=click)
    new_input_btn.grid(row=3, column=0, columnspan=2)
    close_btn = Button(top_5, text="Close", command=root.destroy)
    close_btn.grid(row=4, column=0, columnspan=2)

def click_1():
    global button_3
    global button_4
    global button_5
    global button_6
    top_1 = Toplevel()
    top_1.title("GUI 2")
    button_3 = Button(top_1, text="Alter Table", command=alter)
    button_3.grid(row=0, column=0, columnspan=2)
    button_4 = Button(top_1, text="MATHS", command=click_2)
    button_4.grid(row=1, column=0, columnspan=2)
    button_5 = Button(top_1, text="CHEMISTRY", command=click_3)
    button_5.grid(row=2, column=0, columnspan=2)
    button_6 = Button(top_1, text="BIOLOGY", command=click_4)
    button_6.grid(row=3, column=0, columnspan=2)
    sub_btn = Button(top_1, text="Next Page", command=click_5)
    sub_btn.grid(row=4, column=0, columnspan=2)

def update():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    name_1 = name.get()
    branch_1 = branch.get()
    regd_no_1 = regd_no.get()
    c.execute("""UPDATE students_details
                 SET name = '%s', branch = '%s', regd_no = '%s'
                 WHERE stud_ID = 1""" %(name_1,branch_1,regd_no_1))
    conn.commit()
    print("Updated Successfully")
    conn.close()
def click():
    global button_1
    global button_2
    global name
    global branch
    global regd_no
    top = Toplevel()
    top.title("GUI 1")
    name = Entry(top, width=30)
    name.grid(row=0, column=1)
    branch = Entry(top, width=30)
    branch.grid(row=1, column=1)
    regd_no = Entry(top, width=30)
    regd_no.grid(row=2, column=1)
    name_label = Label(top, text="Name")
    name_label.grid(row=0, column=0)
    branch_label = Label(top, text="Branch")
    branch_label.grid(row=1, column=0)
    regd_no_label = Label(top, text="Registration No.")
    regd_no_label.grid(row=2, column=0)
    button_1 = Button(top, text="Update Record", command=update)
    button_1.grid(row=3, column=0, columnspan=2)
    button_2 = Button(top, text="Next Page", command=click_1)
    button_2.grid(row=4, column=0, columnspan=2)

def popup():
    messagebox.showerror("Error Window", "Invalid username or password")

def login():
    while True:
        user_name_1 = user_name.get()
        pass_word_1 = pass_word.get()
        conn = sqlite3.connect('student.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students_details WHERE username = '%s' AND password = '%s'" %(user_name_1,pass_word_1))
        results = c.fetchall()
        if results:
            print("Welcome")
            break
        else:
            popup()
            break
        conn.commit()
        conn.close()

user_name = Entry(root, textvariable=StringVar(), width=30)
user_name.grid(row=0, column=1)
pass_word = Entry(root, textvariable=StringVar(), width=30)
pass_word.grid(row=1, column=1)
user_name_label = Label(root, text="Username")
user_name_label.grid(row=0, column=0)
pass_word_label = Label(root, text="Password")
pass_word_label.grid(row=1, column=0)
submit_btn = Button(root, text="Login", command=login)
submit_btn.grid(row=2, column=0, columnspan=2)
button_0 = Button(root, text="Next Page", command=click)
button_0.grid(row=3, column=0, columnspan=2)

c.execute("SELECT * FROM students_details WHERE stud_ID = 1")
res = c.fetchall()
print(res)

conn.commit()
conn.close()
root.mainloop()