#Using tkinter to create a GUI application.
from tkinter import * 
from tkinter import ttk

#using self for easy access to all instances in the class
#employee 
class employee:
    def __init__(self,root):
        self.root=root
        self.root.title("CExYtime")
        self.root.geometry("1600x900+0+0") # size of window , width then height

        #Create label for title in frame 
        title = Label(self.root, text="CExYtime employee system", font=("verdana",40,"bold"), bg="blue", fg="white")
        #Using pack method to decare position of widgets. Fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)
        

