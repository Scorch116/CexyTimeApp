import mysql.connector
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox


mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

root=Tk()
root.title("Student Data")
root.geometry("1200x700")

label12=Label(root).grid(row=8,column=5)
label1=Label(root,text="RollNo",width=20,height=2,bg="pink").grid(row=0,column=0)
label2=Label(root,text="First_Name",width=20,height=2,bg="pink").grid(row=1,column=0)
label3=Label(root,text="Last_Name",width=20,height=2,bg="pink").grid(row=2,column=0)
label4=Label(root,text="Phone_Number",width=20,height=2,bg="pink").grid(row=3,column=0)
label5=Label(root,text="City",width=20,height=2,bg="pink").grid(row=4,column=0)
label6=Label(root,text="State",width=20,height=2,bg="pink").grid(row=5,column=0)
label7=Label(root,text="Age",width=20,height=2,bg="pink").grid(row=6,column=0)
label8=Label(root,width=10,height=2).grid(row=7,column=2)
label9=Label(root,width=10,height=2).grid(row=7,column=4)
label10=Label(root,width=10,height=2).grid(row=7,column=6)
label11=Label(root,width=10,height=2).grid(row=7,column=8)
e1=Entry(root,width=30,borderwidth=8)
e1.grid(row=0,column=1)
e2=Entry(root,width=30,borderwidth=8)
e2.grid(row=1,column=1)
e3=Entry(root,width=30,borderwidth=8)
e3.grid(row=2,column=1)
e4=Entry(root,width=30,borderwidth=8)
e4.grid(row=3,column=1)
e5=Entry(root,width=30,borderwidth=8)
e5.grid(row=4,column=1)
e6=Entry(root,width=30,borderwidth=8)
e6.grid(row=5,column=1)
e7=Entry(root,width=30,borderwidth=8)
e7.grid(row=6,column=1)


root.mainloop()