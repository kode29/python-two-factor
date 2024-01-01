import time
import pyotp
import qrcode

key = "EduCodeWithKPSecretPassKey"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="NewUser123", issuer_name="EduCode with KP")

# print(uri)
qrcode.make(uri).save("topt.png")

# def generate_qrcode(text):
#     qr = qrcode.QRCode(
#         version = 1,
#         error_correction = qrcode.constants.ERROR_CORRECT_L,
#         box_size = 10,
#         border = 4,
#     )

#     qr.add_data(text)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save("qrcode001.png")



# generate_qrcode(uri)