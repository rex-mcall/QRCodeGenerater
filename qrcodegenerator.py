import os
import pyqrcode
from pyqrcode import QRCode

# Makes the directory called "generatedCodes" if it doesn't already exist
dirItems = os.listdir() #creates an array of all folders and files in the current working directory
dirExists = False
for x in dirItems:
    if x == "generatedCodes":
        dirExists = True
if dirExists:
    pass
else:
    os.mkdir("generatedCodes") #creates the new directory

urlInput = input("Enter the url: ")
url = pyqrcode.create(urlInput)
name = input("What would you like to call it: ")
url.png('generatedCodes/' + name + '.png', scale = 6)
