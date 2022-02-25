import os
import tkinter.messagebox
from tkinter import *

root_login = Tk()
root_login.geometry('500x500')
root_login.title('Login')
login_bg = PhotoImage(file="background_image.png")

# Show image using label
label1 = Label(root_login, image=login_bg)
label1.place(x=0, y=0)

label2 = Label(root_login).pack(pady=100)


usern = StringVar()
passw = StringVar()


def newroot():
    os.system('main_student_page.py')
    root_login.destroy()


def submit():
    if usern.get() == 'DPS':
        if passw.get() == '@123':
            root_login.destroy()
            newroot()
        else:
            tkinter.messagebox.showerror('error', 'Incorrect Username or Password...')
    else:
        tkinter.messagebox.showerror('error', 'Incorrect Username or Password...')


login_title = Label(root_login, text='Login Page', font=('arial', 20, 'bold')).place(x=175, y=10)

unL = Label(root_login, text='Username', font=('arial', 14, 'bold')).place(x=10, y=75)
unE = Entry(root_login, textvariable=usern, width=15).place(x=150, y=80)

pwL = Label(root_login, text='Password', font=('arial', 14, 'bold')).place(x=10, y=125)
pwE = Entry(root_login, textvariable=passw, width=15).place(x=150, y=130)

submitB = Button(root_login, text='Submit', width=15, height=5, bg='orange', fg='black',
                 command=submit).place(x=200, y=250)

root_login.mainloop()
