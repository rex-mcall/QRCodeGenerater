import pyqrcode
import png
from pyqrcode import QRCode

urlInput = input("Enter the url: ")
url = pyqrcode.create(urlInput)
name = input("What would you like to call it: ")
url.png('qrcodes/' + name + '.png', scale = 6)
