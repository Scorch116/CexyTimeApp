#File is for manager to create rota for staff weekly schdueles
#Using tkinter to create a GUI application.

from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

class createRota:

    def __init__(self,createIndex):
        self.createIndex= createIndex
        self.createIndex.title("CExYtime")
        self.createIndex.geometry("1900x1000+0+0") # size of window , width then height

        #Create label for rota creation title 
        title = Label(self.createIndex, text="CExYtime Rota Creation", font=("verdana",40,"bold"), bg="blue", fg="white")
        #pack method to decare position of widgets,fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)

        rotaCreateFrame = Frame(self.createIndex, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        rotaCreateFrame.place(x=100, y=200, width=1700,height=600)

        #scroll bar  for table 
        #orient = the orientation , horizontial and vertical 
        scroll_x = Scrollbar(rotaCreateFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(rotaCreateFrame, orient=VERTICAL)

        #put the values , before fetching values , create the columns 
        self.createrotaview=ttk.Treeview(rotaCreateFrame,columns=("name","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        #configure scroll to tablevieew
        scroll_x.config(command=self.createrotaview.xview)
        scroll_y.config(command=self.createrotaview.yview)



createIndex=Tk()
object=createRota(createIndex)
createIndex.mainloop()