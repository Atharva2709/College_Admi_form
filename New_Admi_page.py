from tkinter import *
import tkinter.messagebox
import csv

root = Tk()
root.title('New Admission Form')
root.geometry('800x1000')
bg = PhotoImage(file="background_image.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

label2 = Label(root).pack(pady=100)

fn = StringVar()
mn = StringVar()
ln = StringVar()
month = StringVar()
date = StringVar()
year = StringVar()
gender = StringVar()
race = StringVar()
country = StringVar()
phn = StringVar()
email = StringVar()
domain = StringVar()
address = StringVar()
marks_10 = StringVar()
marks_12 = StringVar()


def submit():
    Afn = fn.get()
    Amn = mn.get()
    Aln = ln.get()
    Amonth = month.get()
    Adate = date.get()
    Ayear = year.get()
    Agender = gender.get()
    Arace = race.get()
    Acountry = country.get()
    Aphn = phn.get()
    Aemail = email.get()
    Adomain = domain.get()
    Aaddress = address.get()
    Amarks_10 = marks_10.get()
    Amarks_12 = marks_12.get()

    if Afn == '' or Amn == '' or Aln == '':
        print('Error')
        tkinter.messagebox.showerror('error', 'there was some issue with some information')
        fn.set('')
        mn.set('')
        ln.set('')
        month.set('')
        date.set('')
        gender.set('')
        year.set('')
        race.set('')
        country.set('')
        email.set('')
        domain.set('')
        phn.set('')
        marks_10.set('')
        marks_12.set('')

    else:
        tkinter.messagebox.showinfo('Saved', 'Your info has been saved successfully!')
        with open('Admission.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([Afn, Amn, Aln, Adate, Amonth, Ayear, Agender, Arace, Acountry, Aphn,
                             Aemail, Adomain, Aaddress, Amarks_10, Amarks_12])
        csvfile.close()

    root.destroy()


def clear():
    fn.set('')
    mn.set('')
    ln.set('')
    month.set('')
    date.set('')
    gender.set('')
    year.set('')
    race.set('')
    country.set('')
    email.set('')
    domain.set('')
    phn.set('')
    marks_10.set('')
    marks_12.set('')


countrylst = [
    "Afghanistan",
    "Argentina",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "The Bahrain",
    "Bangladesh",
    "Belgium",
    "Bolivia",
    "Bosnia",
    "Botswana",
    "Brazil",
    "Bulgaria",
    "Burma",
    "Burundi",
    "Cambodia",
    "Canada",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Czechoslovakia",
    "Denmark",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "Finland",
    "France",
    "Germany",
    "Ghana",
    "Greece",
    "Guinea",
    "Hawaii",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Yugoslavia",
    "Kuwait",
    "Lebanon",
    "Libya",
    "Luxembourg",
    "Madagascar",
    "Malaysia",
    "Maldives",
    "Mauritius",
    "Mexico",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Namibia",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Panama",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "South Korea",
    "Romania",
    "Russia",
    "Samoa",
    "Saudi Arabia",
    "Serbia",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sweden",
    "Switzerland",
    "Syria",
    "Texas",
    "Thailand",
    "Turkey",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zimbabwe"]

racelst = [
    "American Indian",
    "Alaskan Native",
    "Asian",
    "Black",
    "Native Hawaiian",
    "Other Pacific Islander",
    "White"]

Title1 = Label(root, text='College Admission Form', font='times 20 bold').place(x=300, y=10)
Title2 = Label(root, text='Enter your admission information below', font='times 10 bold').place(x=335, y=50)

fnl = Label(root, text='First name', font=('arial', 14, 'bold')).place(x=100, y=150)
fne = Entry(root, textvariable=fn, width=10).place(x=400, y=155)

mnl = Label(root, text='Middle name', font=('arial', 14, 'bold')).place(x=100, y=200)
mne = Entry(root, textvariable=mn, width=10).place(x=400, y=205)

lnl = Label(root, text='Last name', font=('arial', 14, 'bold')).place(x=100, y=250)
lne = Entry(root, textvariable=ln, width=10).place(x=400, y=255)

bdl = Label(root, text='Date for Birth', font=('arial', 14, 'bold')).place(x=100, y=300)
datelst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
monthlst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']
yearlst = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
           '2003', '2004', '2005', '2006', '2007', '2008']
droplst_date = OptionMenu(root, date, *datelst).place(x=400, y=300)
date.set('1')
droplst_month = OptionMenu(root, month, *monthlst).place(x=500, y=300)
month.set('January')
droplst_year = OptionMenu(root, year, *yearlst, ).place(x=600, y=300)
year.set('1990')

gl = Label(root, text='Gender', font=('arial', 14, 'bold')).place(x=100, y=350)
genlst = {' Female', ' Male', 'Others'}
droplst_gen = OptionMenu(root, gender, *genlst).place(x=400, y=350)
gender.set('Male')

countryl = Label(root, text='Country', font='arial 14 bold').place(x=100, y=400)
droplst_country = OptionMenu(root, country, *countrylst).place(x=400, y=400)
country.set('----')

racel = Label(root, text='Race', font='arial 14 bold').place(x=100, y=450)
droplst_race = OptionMenu(root, race, *racelst).place(x=400, y=450)
race.set('----')

phnlst = Label(root, text='Contact', font=('arial', 14, 'bold')).place(x=100, y=500)
phnE = Entry(root, textvariable=phn, width=15).place(x=400, y=505)

emailL = Label(root, text='Email Address', font=('arial', 14, 'bold')).place(x=100, y=550)
emailE = Entry(root, textvariable=email, width=25).place(x=400, y=555)
domlst = ['@gmail.com', '@yahoo.com', '@rediff.com', '@outlook.com']
droplst_dom = OptionMenu(root, domain, *domlst).place(x=525, y=550)
domain.set('----')

addressL = Label(root, text='Address', font=('arial', 14, 'bold')).place(x=100, y=600)
addressE = Entry(root, textvariable=address, width=50).place(x=400, y=605)

M_10L = Label(root, text='Marks in 10th Standard', font=('arial', 14, 'bold')).place(x=100, y=650)
M_10E = Entry(root, textvariable=marks_10, width=15).place(x=400, y=655)
M_12L = Label(root, text='Marks in 12th Standard', font=('arial', 14, 'bold')).place(x=100, y=700)
M_12E = Entry(root, textvariable=marks_12, width=15).place(x=400, y=705)

submitB = Button(root, text='Submit', command=submit, bg='orange', fg='white', height=5, width=20) \
    .place(x=150, y=850)
clearB = Button(root, text='Clear', command=clear, bg='orange', fg='white', height=5, width=20) \
    .place(x=500, y=850)

root.mainloop()
