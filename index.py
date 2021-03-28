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

         #------------------------------------------------------------------------------------------------------------#

        #Frame within a Frame at bottom for command buttons , Add , update , Delete and clear!

        leftFrameBottomFrame = Frame(leftFrame, bd="4", bg="blue", relief=RIDGE)
        leftFrameBottomFrame.place(x=15, y=420, width=410,height=60)

        #buttons 
        #when using grid I have start at 0 as it is a new frame.
        add_B = Button(leftFrameBottomFrame, text="ADD", width=10 ,).grid(row=0 , column= 0 , padx=10 , pady=15)
        update_B = Button(leftFrameBottomFrame, text="UPDATE", width=10 ,).grid(row=0 , column= 1 , padx=10 , pady=15)
        delete_B = Button(leftFrameBottomFrame, text="DELETE", width=10 ,).grid(row=0 , column= 2 , padx=10 , pady=15)
        clear_B = Button(leftFrameBottomFrame, text="CLEAR", width=10 ,).grid(row=0 , column= 3 , padx=10 , pady=15)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        #RIGHT SIDE FRAME!
        #Declaring RIGHT side frame 
        rightFrame = Frame(self.root, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        rightFrame.place(x=500, y=85, width=1050,height=560)

        #Label for search box
        #Label for employee staff level - 1,2 or 3
        L_search=Label(rightFrame, text="Search By", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        #Using the combobox for drop down search by "category" e.g. empNo , Name , address.
        C_search=ttk.Combobox(rightFrame , font=("verdana",12 , "bold"), state="readonly") # state needs to be read only so no text can be entered into combo box.
        C_search['values']=("empNo","Name","Staff LVL", "Gender", "Address") # the values to select in the combobox!
        C_search.grid(row=0 , column= 1 , padx=20 , pady= 10, sticky="w" )

        #Text box , to take in search vlaue for the category.
        T_search=Entry(rightFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        T_search.grid(row=0, column=2, padx=20 , pady= 10, sticky="w" )

        #button for commanding search function
        search_B = Button(rightFrame, text="Search", width=10 ,).grid(row=0 , column= 3 , padx=10 , pady=15)
        #Button added for showing results 
        show_B = Button(rightFrame, text="Show", width=10 ,).grid(row=0 , column= 4 , padx=10 , pady=15)

        

        







root=Tk()
object=employee(root)
root.mainloop()


