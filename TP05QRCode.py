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

# QR Code for Redirecting to HCF Website
import segno
from urllib.request import urlopen

png_file_name="TP05TeamAchieversQRCode.png"

website_address = segno.make_qr("https://amitabhthakur856.wixsite.com/humanscarefoundation")
site_url = urlopen("https://static.wixstatic.com/media/d6cc27_a0de5c40d82b4176bf732139363efda7~mv2.png/v1/fill/w_448,h_370,al_c,lg_1,q_85,enc_auto/20221206_004234_0000.png")
website_address.to_artistic(
    background=site_url,
    target="TP05TeamAchieversQRCode.png",
    scale=15,
    light = "lightgreen",
    dark = "green",
    border = 1,
    quiet_zone = "lightgreen"
)
print(f"\nExecuted Successfully!! Find the QR Code named {png_file_name}\n")
