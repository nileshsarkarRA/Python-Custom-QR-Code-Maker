## QR code by Team Achievers 

"""
import segno

qrcode = segno.make_qr("Team Achievers Present QR Code")
qrcode_rotated = qrcode.to_pil(
    scale=10,
    light="green",
    dark="lightgreen",
    border = 0,
    quiet_zone = "lightblue"

).rotate(45, expand=True)
qrcode_rotated.save("TP05QRCode.png")"""

## QR code 
# QR Code for Redirecting to Any website
# Caution
print("""
!! This QR Code doesnt redirect when I used Google Lens. I think its due to the background image quality. Using other QR code scanners works however !!
""")

## Import all relevant modules includeing a redirect urlopener called urlopen and a custom QRCode maker sengo

import segno
from urllib.request import urlopen

#QR Code File name

png_file_name="QRCode.png"

## assign website logo and address relevant variables for opening site
website_address = segno.make_qr("https://github.com/nileshsarkarRA")
website_logo = urlopen("https://logos-world.net/wp-content/uploads/2020/11/GitHub-Logo.png")

# modification to create a custom QRcode
website_address.to_artistic(
    background=website_logo,
    target="QRCode.png",
    scale=15,
    light = "lightblue",
    dark = "white",
    border = 1,
    quiet_zone = "lightgreen"
)
# Display File name and success of operations
print(f"\nExecuted Successfully!! Find the QR Code named {png_file_name}.\n")
