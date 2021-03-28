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

        #Label for Name entry - will start from row 3 using grid
        L_name=Label(leftFrame, text="Name", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_name.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        #textbox entry for employee name 
        T_name=Entry(leftFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        T_name.grid(row=3, column=1, padx=20 , pady= 10, sticky="w" )

         #Label for employee staff level - 1,2 or 3
        L_level=Label(leftFrame, text="Staff LVL", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_level.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        #textbox entry for staff level , can be switch to dropbox
        T_level=Entry(leftFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        T_level.grid(row=4, column=1, padx=20 , pady= 10, sticky="w" )

        #Import "from tkinter import ttk" for the use of combobox!
        #Staff gender
        L_gender=Label(leftFrame, text="Gender", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_gender.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        C_gender=ttk.Combobox(leftFrame , font=("verdana",12 , "bold"), state="readonly") # state needs to be read only so no text can be entered into combo box.
        C_gender['values']=("Male","Female","others") # the values to select in the combobox!
        C_gender.grid(row=5 , column= 1 , padx=20 , pady= 10, sticky="w" )

         #label for Address - must be a text box 
        L_Addr=Label(leftFrame, text="Address",bg="blue", fg="white", font=("verdana",12,"bold") )
        L_Addr.grid(row = 6, column=0 , padx=20 , pady= 10, sticky="w" )
        #text will not be a entry , I have desgined it to be a text box instead of multiple entry.
        self.Address=Text(leftFrame, width=22,height=4, font=("verdana",12 , "bold"))
        self.Address.grid(row=6, column=1, padx=20, pady=10, sticky = "w")


