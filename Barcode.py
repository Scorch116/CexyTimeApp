# Importing Libaries
from pyzbar.pyzbar  import decode # libary to read one-demensional barcodes , using decode to decode the code to get content
import cv2
import time

# capture image with camera window for testing purpose , dont have barcode scanner
# Window size could be altered for main application
capture = cv2.VideoCapture(0)
capture.set(3, 640) # demension for window width
capture.set(4, 480) # demension for window height
camera = True
