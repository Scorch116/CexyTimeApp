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
        
        #------------frame for displaying rota data--------------#
        rotaCreateFrame = Frame(self.createIndex, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        rotaCreateFrame.place(x=100, y=100, width=1700,height=600)

        #scroll bar  for table 
        #orient = the orientation , horizontial and vertical 
        scroll_x = Scrollbar(rotaCreateFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(rotaCreateFrame, orient=VERTICAL)

        #put the values , before fetching values , create the columns 
        self.createrotaview=ttk.Treeview(rotaCreateFrame,columns=("name","Monday_start","Monday_end","Tuesday_start","Tuesday_end","Wednesday_start","Wednesday_end","Thursday_start","Thursday_end","Friday_start","Friday_end","Saturday_start","Saturday_end","Sunday_start","Sunday_end"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.createrotaview=ttk.Treeview(rotaCreateFrame,columns=("name","Monday_start","Monday_end","Tuesday_start","Tuesday_end","Wednesday_start","Wednesday_end","Thursday_start","Thursday_end","Friday_start","Friday_end","Saturday_start","Saturday_end","Sunday_start","Sunday_end"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        #configure scroll to tablevieew
        scroll_x.config(command=self.createrotaview.xview)
        scroll_y.config(command=self.createrotaview.yview)

        #These headings may change
        #Headings for table 
        self.createrotaview.heading("name", text="Name")
        self.createrotaview.heading("Monday_start", text="MONDAY START")
        self.createrotaview.heading("Monday_end", text="MONDAY END")
        self.createrotaview.heading("Tuesday_start", text="TUESDAY START")
        self.createrotaview.heading("Tuesday_end", text="TUESDAY END")
        self.createrotaview.heading("Wednesday_start", text="WEDNESDAY START")
        self.createrotaview.heading("Wednesday_end", text="WEDNESDAY END")
        self.createrotaview.heading("Thursday_start", text="THURSDAY START")
        self.createrotaview.heading("Thursday_end", text="THURSDAY END")
        self.createrotaview.heading("Friday_start", text="FRIDAY START")
        self.createrotaview.heading("Friday_end", text="FRIDAY END")
        self.createrotaview.heading("Saturday_start", text="SATURDAY START")
        self.createrotaview.heading("Saturday_end", text="SATURDAY END")
        self.createrotaview.heading("Sunday_start", text="SUNDAY START")
        self.createrotaview.heading("Sunday_end", text="SUNDAY END")
        #DISPLAY THE HEADINGS
        self.createrotaview['show']='headings'

        #publish table
        self.createrotaview.pack(fill=BOTH,expand=1)

        #--------------------------Bottom frame----------------#
        #Bottom Frame
        #Declaring Bottom frame 
        BottomFrame = Frame(self.createIndex, bd="4", bg="blue", relief=RIDGE)
        BottomFrame.place(x=100, y=710, width=1700,height=280)

        
        #label for employee ID - the employee tag in this case!
        #using grid starting from row 2
        L_eno=Label(BottomFrame, text="empNo", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_eno.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        #textbox entry for employee ID
        self.T_eno=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.T_eno.grid(row=1, column=1, padx=20 , pady= 10, sticky="w" )
        #Label for monday
        L_Monday=Label(BottomFrame, text="Monday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_Monday.grid(row=1, column=9, padx=20, pady=10, sticky="w")
        #textbox entry for Monday start time
        self.start_Monday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_Monday.grid(row=1, column=10, padx=10 , pady= 20, sticky="w" )
        #textbox entry for Monday start time
        self.end_Monday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_Monday.grid(row=1, column=15, padx=10 , pady= 20, sticky="w" )

        #Label for tuesday
        L_Tuesday=Label(BottomFrame, text="Tuesday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_Tuesday.grid(row=2, column=9, padx=20, pady=10, sticky="w")
        #textbox entry for tuesday start time
        self.start_tuesday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_tuesday.grid(row=2, column=10, padx=10 , pady= 20, sticky="w" )
        #textbox entry for Tuesday end time
        self.end_tuesday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_tuesday.grid(row=2, column=15, padx=10 , pady= 20, sticky="w" )

        #Label for Wednesday
        L_Wednesday=Label(BottomFrame, text="Wednesday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_Wednesday.grid(row=3, column=9, padx=20, pady=10, sticky="w")
        #textbox entry for Wednesday start time
        self.start_wednesday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_wednesday.grid(row=3, column=10, padx=10 , pady= 20, sticky="w" )
        #textbox entry for Wednesday end time
        self.end_wednesday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_wednesday.grid(row=3, column=15, padx=10 , pady= 20, sticky="w" )

        #Label for Thrusday
        L_Thursday=Label(BottomFrame, text="Thursday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_Thursday.grid(row=4, column=9, padx=20, pady=10, sticky="w")
        #textbox entry for Thursday start time
        self.start_Thursday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_Thursday.grid(row=4, column=10, padx=10 , pady= 20, sticky="w" )
        #textbox entry for Thursday end time
        self.end_thursday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_thursday.grid(row=4, column=15, padx=10 , pady= 20, sticky="w" )
        

        #Label for Friday
        L_Friday=Label(BottomFrame, text="Friday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_Friday.grid(row=1, column=19, padx=20, pady=10, sticky="w")
        #textbox entry for Friday start time
        self.start_Friday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_Friday.grid(row=1, column=20, padx=10 , pady= 20, sticky="w" )
        #textbox entry for Friday end time
        self.end_Friday=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_Friday.grid(row=1, column=25, padx=10 , pady= 20, sticky="w" )
        

        #Label for Saturday
        L_sat=Label(BottomFrame, text="Saturday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_sat.grid(row=2, column=19, padx=20, pady=10, sticky="w")
        #textbox entry for sat start time
        self.start_sat=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_sat.grid(row=2, column=20, padx=10 , pady= 20, sticky="w" )
        #textbox entry for Friday end time
        self.end_sat=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_sat.grid(row=2, column=25, padx=10 , pady= 20, sticky="w" )

        #Label for Sunday
        L_sun=Label(BottomFrame, text="Sunday", bg="blue", fg="white", font=("verdana",12,"bold"))
        L_sun.grid(row=3, column=19, padx=20, pady=10, sticky="w")
        #textbox entry for sun start time
        self.start_sun=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.start_sun.grid(row=3, column=20, padx=10 , pady= 20, sticky="w" )
        #textbox entry for sun end time
        self.end_sun=Entry(BottomFrame,font=("verdana",12,"bold"), bd=5, relief=GROOVE)
        self.end_sun.grid(row=3, column=25, padx=10 , pady= 20, sticky="w" )

        #FRAME FOR COMMAND BUTTONS
        buttonFrame = Frame(BottomFrame, bd="4", bg="blue", relief=RIDGE)
        buttonFrame.place(x=5, y=120, width=380,height=60)
        

        add_B = Button(buttonFrame, text="ADD", width=10 ,command= self.add_shift).grid(row=4 , column= 19 , padx=5 , pady=10)
        update_B = Button(buttonFrame, text="UPDATE", width=10 ,).grid(row=4 , column= 20 , padx=5 , pady=10)
        delete_B = Button(buttonFrame, text="DELETE", width=10 ,).grid(row=4 , column= 21 , padx=5 , pady=10)
        show_B = Button(buttonFrame, text="SHOW", width=10 ,command=self.display_data).grid(row=4 , column= 22 , padx=5 , pady=10)
        

#---------------------------ADD SHIFT FUNCTION------------------#

#function to add shift to DB 
    def add_shift(self): 
        #select statement
        empID = self.T_eno.get()
        mon_start=self.start_Monday.get()
        mon_end=self.end_Monday.get()
        tues_start=self.start_tuesday.get()
        tues_end=self.end_tuesday.get()
        wed_start=self.start_wednesday.get()
        wed_end=self.end_wednesday.get()
        thur_start=self.start_Thursday.get()
        thur_end=self.end_thursday.get()
        fri_start=self.start_Friday.get()
        fri_end=self.end_Friday.get()
        sat_start=self.start_sat.get()
        sat_end=self.end_sat.get()
        sun_start=self.start_sun.get()
        sun_end=self.end_sun.get()
        #must use update ass the empID is added from manager index page
        update = "UPDATE shifts SET mon_start='%s', mon_end='%s',tues_start='%s', tues_end='%s', wed_start='%s', wed_end='%s', thur_start='%s',thur_end='%s',fri_start='%s',fri_end='%s',sat_start='%s',sat_end='%s',sun_start='%s',sun_end='%s' where empID='%s'" %(mon_start,mon_end,tues_start,tues_end,wed_start,wed_end,thur_start,thur_end,fri_start,fri_end,sat_start,sat_end,sun_start,sun_end,empID)
        mycursor.execute(update)
        mydb.commit()
        messagebox.askokcancel("INFO","Shift added")
        #delete statements
        self.start_Monday.delete(0,END)
        self.end_Monday.delete(0,END)
        self.start_tuesday.delete(0,END)
        self.end_tuesday.delete(0,END)
        self.start_wednesday.delete(0,END)
        self.end_wednesday.delete(0,END)            
        self.start_Thursday.delete(0,END)
        self.end_thursday.delete(0,END)
        self.start_Friday.delete(0,END)
        self.end_Friday.delete(0,END)
        self.start_sat.delete(0,END)
        self.end_sat.delete(0,END)
        self.start_sun.delete(0,END)
        self.end_sun.delete(0,END)
        self.T_eno.delete(0,END)

        #recall data to display
        self.display_data()

    
    #display data function 

    def display_data(self):
        #method will remove previous data
        self.createrotaview.delete(*self.createrotaview.get_children())
        #select statement to get data from DB
        select = "select person.name,shifts.mon_start,shifts.mon_end,shifts.tues_start,shifts.tues_end,shifts.wed_start,shifts.wed_end,shifts.thur_start,shifts.thur_end,shifts.fri_start,shifts.fri_end,shifts.sat_start,shifts.sat_end,shifts.sun_start,shifts.sun_end from person INNER JOIN shifts on person.empno=shifts.empID;"
        mycursor.execute(select)
        result=mycursor.fetchall()
        name=""
        mon_start=""
        mon_end=""
        tues_start=""
        tues_end=""
        wed_start=""
        wed_end=""
        thur_start=""
        thur_end=""
        fri_start=""
        fri_end=""
        sat_start=""
        sat_end=""
        sun_start=""
        sun_end=""
        #for loop to iterate through results
        for i in result:
            name =i[0]
            mon_start= i[1]
            mon_end=i[2]
            tues_start=i[3]
            tues_end=i[4]
            wed_start=i[5]
            wed_end=i[6]
            thur_start=i[7]
            thur_end=i[8]
            fri_start=i[9]
            fri_end=i[10]
            sat_start=i[11]
            sat_end=i[12]
            sun_start=i[13]
            sun_end=i[14]
            #insert statement to inert data into treeview for dispaly
            self.createrotaview.insert("",'end',text=name,values=(name,mon_start,mon_end,tues_start,tues_end,wed_start,wed_end,thur_start,thur_end,fri_start,fri_end,sat_start,sat_end,sun_start,sun_end))
        mydb.commit()
    
    



                



    


createIndex=Tk()
object=createRota(createIndex)
object.display_data()
createIndex.mainloop()