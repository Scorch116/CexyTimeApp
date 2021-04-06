#staff index to view rota 

#Using tkinter to create a GUI application.

from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

#sql connector 
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

class rota:

    def __init__(self,rotaindex):
        self.rotaindex = rotaindex
        self.rotaindex.title("CExYtime")
        self.rotaindex.geometry("1900x700+0+0") # size of window , width then height

        #Create label for title in frame 
        title = Label(self.rotaindex, text="CExYtime Rota", font=("verdana",40,"bold"), bg="blue", fg="white")
        #Using pack method to decare position of widgets. Fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)
