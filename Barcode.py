# Importing Libaries
from pyzbar.pyzbar  import decode # libary to read one-demensional barcodes , using decode to decode the code to get content
import cv2
import time
from tkinter import messagebox
import mysql.connector

#SQL connector for CEx database
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database ="cexydatabase"
)

mycursor =mydb.cursor()

#Select statment to get empNo


# capture image with camera window for testing purpose , dont have barcode scanner
# Window size could be altered for main application
capture = cv2.VideoCapture(0)
capture.set(3, 640) # demension for window width
capture.set(4, 480) # demension for window height
camera = True

staff_tags =["_10282_"] # will be used to add ID of staff for testing , should be hardcoded for test

while camera == True: # camera will stay open for scanning (testing make sure to change to false for conditioing later in application)
    success, frame = capture.read()  # frame is the data we need
    

    for code in decode(frame):  # for loop used for capturing data from the frame
        #convert theo decoded data to string to store in list 
        string_code=str(code.data.decode('utf-8'))
        if string_code not in staff_tags: 

            tStamp = time.time() # used for time stamping 
            print('Recorded time :', tStamp) 
            print('Welcome')
            #Keep these varibles for for testing purposes
            #print(code.type)  # testing purpose will show the type of data
            #print(code.data.decode('utf-8')) # will decode and dispaly data , decoding using utf-8
            print(string_code)
            from index import employee
        
            
            time.sleep(3) # set time til next scan , not gonna set for 1 second cause it scans way to quick.
            cv2.destroyAllWindows()
           

        elif code.data.decode('utf-8') not in staff_tags: # condition for invald tag
            print("Error , please contact manager")
        
        else:
            pass
    cv2.imshow('CexyFrame',frame) 
    cv2.waitKey(1)


    


