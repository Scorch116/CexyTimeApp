#login page for CexyTime application 

#Using tkinter to create a GUI application.

from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

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
        pass


root=Tk()
object=login(root)
root.mainloop()