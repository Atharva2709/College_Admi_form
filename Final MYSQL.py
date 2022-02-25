import mysql.connector as sqltor

mydb = sqltor.connect(host="localhost", user="root", passwd="abcd", database='atharva')


def Main_Menu():
    print('\n')
    print(60 * '*')
    print('***Welcome to school management system***')
    print('1. Add New Student detail...')
    print('2. Display all student detail...')
    print('3. Update student\'s details...')
    print('4. Delete student\'s details...')
    print(50 * '=')
    print('5. Add new student\'s examination details...')
    print('6. Display all student\'s examination details...')
    print('7. Update student\'s examination details...')
    print('8. Delete student\'s examination details...')
    print('9. Exit')
    print(60 * '*')


def addStud():
    a1 = input('Enter Roll Number : ')
    a2 = input('Enter Name : ')
    a3 = input('Enter Father\'s name : ')
    a4 = input('Enter Mother\'s name : ')
    a5 = input('Enter Address : ')
    a6 = input('Enter Phone Number : ')
    a7 = input('Enter E-mail : ')

    data = (a1, a2, a3, a4, a5, a6, a7)
    sql = 'insert into s1 values(%s,%s,%s,%s,%s,%s,%s)'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    print('\nData Entered Successfully...')


def displayStud():
    sql = 'Select * from s1'
    c1 = mydb.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print(i)


def updateStud():
    print('\nEnter student details you want to be update : ')
    a1 = input('Enter Roll Number : ')
    a2 = input('Enter Name : ')
    a3 = input('Enter Father\'s name : ')
    a4 = input('Enter Mother\'s name : ')
    a5 = input('Enter Address : ')
    a6 = input('Enter Phone Number : ')
    a7 = input('Enter E-mail : ')

    data = (a2, a3, a4, a5, a6, a7, a1)
    sql = 'update s1 set name = %s, father_name = %s,' \
          ' mother_name = %s, address = %s, phone = %s, email = %s where roll_no = %s'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    print('\nData Updated Successfully...')


def deleteStud():
    print('\nEnter student\'s roll number you want to delete : ')
    a1 = input('Enter Roll Number : ')

    data = (a1,)
    sql = 'Delete from s1 where roll_no = %s'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    print('\nData Updated Successfully...')


def addStudExam():
    a1 = input('Enter Roll Number : ')
    a2 = input('Enter Name : ')
    a3 = input('Enter Class : ')
    a4 = input('Enter Section : ')
    a5 = input('Enter Total Marks (Out of 500) : ')
    a6 = input('Enter Percentage : ')
    a7 = input('Enter Grade : ')

    data = (a1, a2, a3, a4, a5, a6, a7)
    sql = 'insert into s2 values(%s,%s,%s,%s,%s,%s,%s)'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    print('\nData Entered Successfully...')


def displayStudExam():
    sql = 'Select * from s2'
    c1 = mydb.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print(i)


def updateStudExam():
    print('\nEnter student detail you want to update : ')
    a1 = input('Enter Roll Number : ')
    a2 = input('Enter Name : ')
    a3 = input('Enter Class : ')
    a4 = input('Enter Section : ')
    a5 = input('Enter Total Marks (Out of 500) : ')
    a6 = input('Enter Percentage : ')
    a7 = input('Enter Grade : ')

    data = (a2, a3, a4, a5, a6, a7, a1)
    sql = 'update s2 set Name = %s, Class = %s, Section = %s, TotalMarks = %s, Percentage = %s,' \
          ' Grade = %s where Rno = %s'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    print('\nData Updated Successfully...')


def deleteStudExam():
    print('\nEnter student roll number you want to delete : ')
    a1 = input('Enter Roll Number : ')

    data = (a1,)
    sql = 'Delete from s2 where Rno = %s'
    c1 = mydb.cursor()
    c1.execute(sql, data)
    mydb.commit()
    print('\nData Deleted Successfully...')


while True:
    Main_Menu()
    ch = input('Enter your choice : ')
    if ch == '1':
        addStud()
    elif ch == '2':
        displayStud()
    elif ch == '3':
        updateStud()
    elif ch == '4':
        deleteStud()
    elif ch == '5':
        addStudExam()
    elif ch == '6':
        displayStudExam()
    elif ch == '7':
        updateStudExam()
    elif ch == '8':
        deleteStudExam()
    elif ch == '9':
        break
    else:
        print('\n***Enter a valid Choice***')
