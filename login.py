#login page for CexyTime application 

#Using tkinter to create a GUI application.

from tkinter import * 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

#varibale for SQl connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

#login class , init definiton for varible access.
class login:
    def __init__(self,root) :
        self.root=root
        self.root.title("CExYtime")
        self.root.geometry("1900x1000+0+0") # size of window , width then height

        #Create label for title in frame 
        title = Label(self.root, text="CExYtime Login", font=("verdana",40,"bold"), bg="blue", fg="white")
        #Using pack method to decare position of widgets. Fill with X will fill the window with the brackground colour for tidyness.
        title.pack(side=TOP, fill=X)

        #Declaring main side frame 
        mainFrame = Frame(self.root, bd="4", bg="blue", relief=RIDGE)
        #must "place" for visibility.
        mainFrame.place(x=650, y=85, width=600,height=700)

        #declaring canvas varible for application
        canvas = ttk.Canvas(self.root, width = 500, height = 250)

        canvas.pack()

        #using the PIL library, we imported a photo onto our window and assigned it to my_img
        my_img = ImageTk.PhotoImage(Image.open("CEx logo.jpeg"))

        #putting image in parameter
        canvas.create_image(125, 20, ANCHOR = NW, image= my_img)



        # label widget is a standard Tkinter widget used to display a text or image on the screen
        # in this case, I assigned an image to the label and packed it onto the window
        #my_Label = ttk.Label(mainFrame, image=my_img)
        #my_Label.pack(side=LEFT,fill=BOTH)




root=Tk()
object=login(root)
root.mainloop()