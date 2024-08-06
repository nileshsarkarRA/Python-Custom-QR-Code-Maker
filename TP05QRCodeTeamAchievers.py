## QR code by Team Achievers 
# QR Code for Redirecting to HCF Website
# Caution
print("""
!! This QR Code doesnt redirect when we used Google Lens. We think its due to the background image quality. Using other QR code scanners works however !!
""")

## Import all relevant modules includeing a redirect urlopener called urlopen and a custom QRCode maker sengo

import segno
from urllib.request import urlopen

#QR Code File name

png_file_name="TP05TeamAchieversQRCode.png"

## assign website logo and address relevant variables for opening site
website_address = segno.make_qr("https://amitabhthakur856.wixsite.com/humanscarefoundation")
website_logo = urlopen("https://static.wixstatic.com/media/d6cc27_a0de5c40d82b4176bf732139363efda7~mv2.png/v1/fill/w_448,h_370,al_c,lg_1,q_85,enc_auto/20221206_004234_0000.png")

# modification to create a custom QRcode
website_address.to_artistic(
    background=website_logo,
    target="TP05TeamAchieversQRCode.png",
    scale=15,
    light = "lightgreen",
    dark = "green",
    border = 1,
    quiet_zone = "lightgreen"
)
# Display File name and success of operations
print(f"\nExecuted Successfully!! Find the QR Code named {png_file_name} to redirect to Humans Care Foundation Website.\n")
