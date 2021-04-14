#staff index to view rota 

#Using tkinter to create a GUI application.


from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import time
import timestamp


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
        self.rotaindex.geometry("1900x1000+0+0") # size of window , width then height

        #Create label for title in frame 
        title = Label(rotaindex, text="CExYtime Rota", font=("verdana",40,"bold"), bg="blue", fg="white")
        #Using pack method to decare position of widgets. Fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)
        #-------------------Clock Frame---------------------#
        clockFrame = Frame(rotaindex, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        clockFrame.place(x=100, y=90, width=1700,height=100)

        #-----------label + function for time---------#

        def display_time():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            current_time = hour + ":" + minute + ":" +second
            time_label ['text'] = current_time
            #using the after method , first attribute is in milliseconds , 1000 milliseconds is 1 second
            #cause window to respond to window counting down to 0 from 1000 miliseconds
            #as soon as it reaches zero , it will execute the diplay_time funtion again.
            clockFrame.after(1000,display_time)

        
        time_label = Label(clockFrame, font=('Verdana',50), fg='white', bg='blue')
        time_label.pack(padx=300,pady=10)
        display_time()
        #time_label.config(text=hour + ":" + minute + ":" +second)
        

        #----------------------Frame for displaying data-------------------------#
        rotaFrame = Frame(self.rotaindex, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        rotaFrame.place(x=100, y=200, width=1700,height=600)

        #scroll bar  for table 
        #orient = the orientation , horizontial and vertical 
        scroll_x = Scrollbar(rotaFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(rotaFrame, orient=VERTICAL)

        #put the values , before fetching values , create the columns 
        self.rotaview=ttk.Treeview(rotaFrame,columns=("name","Monday_start","Monday_end","Tuesday_start","Tuesday_end","Wednesday_start","Wednesday_end","Thursday_start","Thursday_end","Friday_start","Friday_end","Saturday_start","Saturday_end","Sunday_start","Sunday_end"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        #configure scroll to tablevieew
        scroll_x.config(command=self.rotaview.xview)
        scroll_y.config(command=self.rotaview.yview)

        #These headings may change
        #Headings for table 
        self.rotaview.heading("name", text="Name")
        self.rotaview.heading("Monday_start", text="MONDAY START")
        self.rotaview.heading("Monday_end", text="MONDAY END")
        self.rotaview.heading("Tuesday_start", text="TUESDAY START")
        self.rotaview.heading("Tuesday_end", text="TUESDAY END")
        self.rotaview.heading("Wednesday_start", text="WEDNESDAY START")
        self.rotaview.heading("Wednesday_end", text="WEDNESDAY END")
        self.rotaview.heading("Thursday_start", text="THURSDAY START")
        self.rotaview.heading("Thursday_end", text="THURSDAY END")
        self.rotaview.heading("Friday_start", text="FRIDAY START")
        self.rotaview.heading("Friday_end", text="FRIDAY END")
        self.rotaview.heading("Saturday_start", text="SATURDAY START")
        self.rotaview.heading("Saturday_end", text="SATURDAY END")
        self.rotaview.heading("Sunday_start", text="SUNDAY START")
        self.rotaview.heading("Sunday_end", text="SUNDAY END")
        #DISPLAY THE HEADINGS
        self.rotaview['show']='headings'

        #publish table
        self.rotaview.pack(fill=BOTH,expand=1)

        




        #--------------------Clock in button-----------------#

        clockinFrame = Frame(self.rotaindex, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        clockinFrame.place(x=100, y=820, width=1700,height=150)
        #button for clocking in 
        clockin_B = Button(clockinFrame, text="Clockin", width=235 ,height= 7,command=timestamp.returnTime).grid(row=0 , column= 0 , padx=10 , pady=15)

        
       #display data function 

    def display_data(self):
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
            self.rotaview.insert("",'end',text=name,values=(name,mon_start,mon_end,tues_start,tues_end,wed_start,wed_end,thur_start,thur_end,fri_start,fri_end,sat_start,sat_end,sun_start,sun_end))
        mydb.commit()
       


rotaindex=Tk()
object=rota(rotaindex)
object.display_data()
rotaindex.mainloop()