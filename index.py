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
        
        #Declaring Left side frame 
        leftFrame = Frame(self.root, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        leftFrame.place(x=20, y=85, width=450,height=560)
        #title for frame
        ftitle=Label(leftFrame, text="Manage Employee",bg="blue", fg="white", font=("verdan",20,"bold"))
        #in the frame using gird - organises the lebels in a table strutuce in the parent widget and set position
        #colspan is column space , so i am merging 2 columns.
        ftitle.grid(row=0,columnspan=2, padx=20, pady=20, sticky="w")

        #label for employee ID - the employee tag in this case!
        #using grid starting from row 2
        L_eno=Label(leftFrame, text="empNo", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_eno.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        #textbox entry for employee ID
        T_eno=Entry(leftFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        T_eno.grid(row=2, column=1, padx=20 , pady= 10, sticky="w" )

