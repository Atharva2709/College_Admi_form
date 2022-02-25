from tkinter import *
import os

root_lan_page = Tk()
root_lan_page.geometry('1000x500')
root_lan_page.title('College Management System')

lan_bg = PhotoImage(file='background_image.png')

# Show image using label
label1 = Label(root_lan_page, image=lan_bg)
label1.place(x=0, y=0)

label2 = Label(root_lan_page).pack(pady=100)


lan_title = Label(root_lan_page, text='Welcome to College Management System', font=('arial', 20, 'bold'))\
    .place(x=225, y=10)
lan_desc = Label(root_lan_page, text='This is a very advanced Tkinter-Python-MYSQL Management System',
                 font=('arial', 18, 'bold', 'italic')).place(x=100, y=50)


def login():
    os.system('Login_page.py')


def newadmi():
    os.system('New_Admi_page.py')


def close():
    root_lan_page.destroy()


naB = Button(root_lan_page, text='New Admission', bg='orange', fg='black', height=5, width=20,
             command=lambda: newadmi()).place(x=200, y=250)
loginB = Button(root_lan_page, text='Login', bg='orange', fg='black', height=5, width=20,
                command=lambda: login()).place(x=450, y=250)
close_B = Button(root_lan_page, text='Close', bg='orange', fg='black', height=5, width=20,
                 command=lambda: close()).place(x=710, y=250)
root_lan_page.mainloop()
