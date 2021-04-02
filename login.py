#login page for CexyTime application 

#Using tkinter to create a GUI application.

from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

#varibale for SQl connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

#login class , init definiton for varible access.
class login:
    def __init__(self,root) :
        self.root=root
        self.root.title("CExYtime")
        self.root.geometry("1700x1000+0+0") # size of window , width then height

        #Create label for title in frame 
        title = Label(self.root, text="CExYtime Login", font=("verdana",40,"bold"), bg="blue", fg="white")
        #Using pack method to decare position of widgets. Fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)

        #Declaring main side frame 
        mainFrame = Frame(self.root, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        mainFrame.place(x=600, y=85, width=600,height=700)

        #label for Username 
        #using grid starting from row3
        L_username=Label(mainFrame, text="Username", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_username.grid(row=3, column=1, padx=75, pady=50, sticky="w")
        #textbox entry for username
        T_username=Entry(mainFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        T_username.grid(row=3, column=2, padx=25, pady= 50, sticky="w" )

        #label for password
        #using grid starting from row 4
        L_password=Label(mainFrame, text="Password", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_password.grid(row=4, column=1, padx=75, pady=10, sticky="w")
        #textbox entry for password
        T_password=Entry(mainFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        T_password.grid(row=4, column=2, padx=25, pady= 10, sticky="w" )

        #Frame for buttons added

        buttonFrame = Frame(mainFrame, bd="4", bg="blue", relief=RIDGE)
        buttonFrame.place(x=35, y=350, width=500,height=150)

        #buttons
        loginbtn = Button(buttonFrame, text="LOGIN", width=65,height=7,).grid(row=0 , column= 0 , padx=10 , pady=15)
        



    
    def login():
        pass




      


root=Tk()
object=login(root)
root.mainloop()