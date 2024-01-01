import time
import pyotp

key = "EduCodeWithKPSecretPassKey"

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter 2FA Code: ")))