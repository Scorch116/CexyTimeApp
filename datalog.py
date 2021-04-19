#Using tkinter to create a GUI application.

from tkinter import * 
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

#using self for easy access to all instances in the class

class datalog:

    def __init__(self,logindex):
        self.index=logindex
        self.index.title("CExYtime")
        self.index.geometry("1900x1000+0+0") # size of window , width then height
        
        #Create label for title in frame 
        title = Label(self.index, text="CExYtime Clockin Log", font=("verdana",40,"bold"), bg="blue", fg="white")
        #Using pack method to decare position of widgets. Fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)
        
        #Declaring frame 
        MainFrame = Frame(self.index, bd="4", bg="white", relief=RIDGE)
        #must "place" for visibility.
        MainFrame.place(x=600, y=100, width=700,height=700)

        
        
        #frame for text
        self.text_widget = tk.Text(MainFrame, height=100, width=100)
        scroll_bar = tk.Scrollbar(MainFrame,orient=VERTICAL)
        scroll_bar.pack(side=tk.RIGHT, fill=Y)
        self.text_widget.pack(side=tk.LEFT)

        #Declaring button frame 
        btnFrame = Frame(self.index, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        btnFrame.place(x=600, y=850, width=700,height=95)

        refreshbtn = Button(btnFrame, text="REFRESH", width=97 ,height=5,command=self.readData).grid(row=0 , column= 0 , padx=0 , pady=0)

        
    def readData(self):

        self.text_widget.delete(*self.text_widget.get_children())
        #function to open file
        datafile=open("LOGIN Time Log.txt", "r")
        readfile=datafile.read()
        #insert text from doc into text widget
        self.text_widget.insert(tk.END,readfile)

        








                 
logindex=Tk()
object=datalog(logindex)
object.readData()
logindex.mainloop()