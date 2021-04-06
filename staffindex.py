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
        self.rotaview=ttk.Treeview(rotaFrame,columns=("name","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        #configure scroll to tablevieew
        scroll_x.config(command=self.rotaview.xview)
        scroll_y.config(command=self.rotaview.yview)

        #These headings may change
        #Headings for table 
        self.rotaview.heading("name", text="Name")
        self.rotaview.heading("Monday", text="MONDAY")
        self.rotaview.heading("Tuesday", text="TUESDAY")
        self.rotaview.heading("Wednesday", text="WEDNESDAY")
        self.rotaview.heading("Thursday", text="THURSDAY")
        self.rotaview.heading("Friday", text="FRIDAY")
        self.rotaview.heading("Saturday", text="SATURDAY")
        self.rotaview.heading("Sunday", text="SUNDAY")
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

        
    
       


rotaindex=Tk()
object=rota(rotaindex)
rotaindex.mainloop()