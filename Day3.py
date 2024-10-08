#  QR Code Generator


import qrcode                # This imports the qrcode library, which is used to generate QR codes
from PIL import Image    
# This imports the Image class from the Python Imaging Library (PIL), used for opening, manipulating, and saving images


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)
# qr = qrcode.QRCode(...): This creates a new instance of the QRCode class, initializing the QR code object with specific parameters:
# version=1: Specifies the size of the QR code, where 1 is the smallest (21x21 matrix). Higher numbers produce larger QR codes that can store more data.
# error_correction=qrcode.constants.ERROR_CORRECT_H: Sets the error correction level to H, which means the QR code can be restored even if up to 30% of it is damaged or obscured. The other options are:
# L: ~7% error recovery.
# M: ~15% error recovery.
# Q: ~25% error recovery.
# H: ~30% error recovery.
# box_size=10: Determines the size of each individual box (or "pixel") in the QR code, with 10 meaning each box is 10x10 pixels.
# border=4: Specifies the width of the border (or margin) around the QR code, with a value of 4 meaning a 4-box wide border.




qr.add_data("https://www.youtube.com/@QrioFyte")

# This method adds the data (in this case, a URL to a YouTube channel) to the QR code. 
# The QR code will encode this data so that when scanned, it directs the user to the provided URL.


qr.make(fit=True)

#This finalizes the QR code's design. The fit=True argument allows the QR code library to automatically adjust the dimensions of the QR code to the minimum size necessary to fit the data.

img=qr.make_image(fill_color="white", back_color="black")



img.save("QrioFyte.png")

# img.save("QrioFyte.png"): This saves the generated QR code image as a PNG file named QrioFyte.png. The image is saved in the same directory where the script is run.


#----------------------------------------------------------------Short Trick ---------------------------------------------------------------------------------------------------------------------------


import qrcode as qr
image = qr.make("https://www.youtube.com/@QrioFyte")
image.save("QrioFyte_youtube.png")
