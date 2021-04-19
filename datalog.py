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
        MainFrame = Frame(self.index, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        MainFrame.place(x=600, y=100, width=700,height=700)

        #function to open file
        datafile=open("LOGIN Time Log.txt", "r")
        readfile=datafile.read()
        
        #frame for text
        text_widget = tk.Text(MainFrame, height=100, width=100)
        scroll_bar = tk.Scrollbar(logindex)
        scroll_bar.pack(side=tk.RIGHT)
        text_widget.pack(side=tk.LEFT)

        #insert text from doc into text widget
        text_widget.insert(tk.END,readfile)










                 
logindex=Tk()
object=datalog(logindex)
logindex.mainloop()