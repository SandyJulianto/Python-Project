# Import modules
import pyqrcode
import pyqrcode import QRCode
import png
# Enter link for QR
n = input("Enter a link : ")
# Create QR code from n 
url = pyqrcode.create(n)
# Create and save QR code with svg format image and name it myqr.svg
url.svg("myqr.svg", scale = 8)
# Create and save QR code with png format image and name it myqr.png
url.png("mysqr.png", scale = 6)