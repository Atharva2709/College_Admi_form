from tkinter import *
import tkinter.messagebox
import mysql.connector as sqltor

mydb = sqltor.connect(host="localhost", user="root", passwd="abcd", database='college_admi')

root_stu = Tk()
root_stu.geometry('850x500')
root_stu.title('Student Details')
stu_bg = PhotoImage(file="background_image.png")

# Show image using label
label1 = Label(root_stu, image=stu_bg)
label1.place(x=0, y=0)

label2 = Label(root_stu).pack(pady=100)


stu_name = StringVar()
stu_grade = StringVar()
stu_section = StringVar()
stu_admi = StringVar()
stu_phy = StringVar()
stu_chem = StringVar()
stu_maths = StringVar()
stu_compsci = StringVar()
stu_eng = StringVar()


def addStud():
    a1 = stu_name.get()
    a2 = stu_grade.get()
    a3 = stu_section.get()
    a4 = stu_admi.get()

    data_s1 = (a1, a2, a3, a4)
    sql_s1 = 'insert into s1 values(%s,%s,%s,%s)'
    c1 = mydb.cursor()
    c1.execute(sql_s1, data_s1)
    mydb.commit()
    tkinter.messagebox.showinfo('Message', 'Record added successfully')


def deleteStud():
    tkinter.messagebox.askquestion('Delete student record', 'Are you sure you want to delete the record?')
    a4 = stu_admi.get()

    data = (a4,)
    sql_s1 = 'Delete from s1 where admi_no = %s'
    c1 = mydb.cursor()
    c1.execute(sql_s1, data)
    mydb.commit()
    tkinter.messagebox.showinfo('Message', 'Record deleted successfully')


def addStudExam():
    a1 = stu_name.get()
    a2 = stu_grade.get()
    a3 = stu_section.get()
    a4 = stu_admi.get()
    a5 = stu_phy.get()
    a6 = stu_chem.get()
    a7 = stu_maths.get()
    a8 = stu_compsci.get()
    a9 = stu_eng.get()

    data = (a1, a2, a3, a4, a5, a6, a7, a8, a9)
    sql = 'insert into s2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    tkinter.messagebox.showinfo('Message', 'Record added successfully')


def deleteStudExam():
    tkinter.messagebox.askquestion('Delete Record', 'Are you sure you want to delete this record?')
    a4 = stu_admi.get()

    data = (a4,)
    sql = 'Delete from s2 where admi_no = %s'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    tkinter.messagebox.showinfo('Message', 'Record deleted successfully')


def logout():
    root_stu.destroy()


St = Label(root_stu, text='Student Details', font=('arial', 20, 'bold')).place(x=300, y=10)

nL = Label(root_stu, text='Name', font=('arial', 12, 'bold')).place(x=10, y=75)
nE = Entry(root_stu, textvariable=stu_name, width=15).place(x=100, y=80)

gL = Label(root_stu, text='Class', font=('arial', 12, 'bold')).place(x=10, y=100)
gE = Entry(root_stu, textvariable=stu_grade, width=15).place(x=100, y=105)

sL = Label(root_stu, text='Section', font=('arial', 12, 'bold')).place(x=10, y=125)
sE = Entry(root_stu, textvariable=stu_section, width=15).place(x=100, y=130)

aL = Label(root_stu, text='Admi No.', font=('arial', 12, 'bold')).place(x=10, y=150)
aE = Entry(root_stu, textvariable=stu_admi, width=15).place(x=100, y=155)

pL = Label(root_stu, text='Physics', font=('arial', 12, 'bold')).place(x=10, y=200)
pE = Entry(root_stu, textvariable=stu_phy, width=10).place(x=10, y=225)

chL = Label(root_stu, text='Chemistry', font=('arial', 12, 'bold')).place(x=145, y=200)
chE = Entry(root_stu, textvariable=stu_chem, width=10).place(x=155, y=225)

mL = Label(root_stu, text='Mathematics', font=('arial', 12, 'bold')).place(x=300, y=200)
mE = Entry(root_stu, textvariable=stu_maths, width=10).place(x=315, y=225)

coL = Label(root_stu, text='Computer Science', font=('arial', 12, 'bold')).place(x=475, y=200)
coE = Entry(root_stu, textvariable=stu_compsci, width=10).place(x=510, y=225)

eL = Label(root_stu, text='English', font=('arial', 12, 'bold')).place(x=700, y=200)
eE = Entry(root_stu, textvariable=stu_eng, width=10).place(x=700, y=225)

add_stuB = Button(root_stu, text='Add Record', command=lambda: addStud()).place(x=100, y=400)
del_stuB = Button(root_stu, text='Delete Record', command=lambda: deleteStud()).place(x=300, y=400)
add_marksB = Button(root_stu, text='Add Marks', command=lambda: addStudExam()).place(x=500, y=400)
del_marksB = Button(root_stu, text='Delete Marks', command=lambda: deleteStudExam()).place(x=700, y=400)
logout_B = Button(root_stu, text='Logout', command=lambda: logout()).place(x=775, y=10)

root_stu.mainloop()
