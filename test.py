import mysql.connector
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

#varibale for SQl connector
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()


class accountCheck:
    def __init__(self,check) :
        self.check=check
        self.check.title("CExYtime")
        self.check.geometry("430x220+0+0") # size of window , width then height

        #Declaring main side frame 
        mainFrame = Frame(self.check, bd="4", bg="black", relief=RIDGE)
        #must "place" for visibility.
        mainFrame.place(x=0, y=0, width=430,height=220)

        #label for first ID
        L_first_username=Label(mainFrame, text="First ID", bg="black", fg="white", font=("verdana",12,"bold"))
        L_first_username.grid(row=0, column=0, padx=25, pady=15, sticky="w")
        #textbox entry for first ID
        self.T_first_username=Entry(mainFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.T_first_username.grid(row=0, column=1, padx=25, pady= 15, sticky="w" )

        #label for second ID
        L_second_username=Label(mainFrame, text="Second ID", bg="black", fg="white", font=("verdana",12,"bold"))
        L_second_username.grid(row=1, column=0, padx=25, pady=15, sticky="w")
        #textbox entry for second ID
        self.T_second_username=Entry(mainFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.T_second_username.grid(row=1, column=1, padx=25, pady= 15, sticky="w" )
        

        #Frame for buttons added

        buttonFrame = Frame(mainFrame, bd="4", bg="black")
        buttonFrame.place(x=10, y=150, width=400,height=50)
        #buttons
        loginbtn = Button(buttonFrame, text="CONFIRM", width=55,height=2,).grid(row=4 , column= 0 , padx=0 , pady=0)

    #fucntion to confirm ID of staff for shift exchange 
    def confirmID(self):
        #declaring varibles for the username entry.
        ID1 = self.T_first_username.get()
        ID2 = self.T_second_username.get()
        #delete fields 
        self.T_first_username.delete(0,END)
        self.T_second_username.delete(0,END)
        #sql select statement to retrieve username from database
        



check=Tk()
object=accountCheck(check)
check.mainloop()