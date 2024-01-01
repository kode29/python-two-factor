import time
import pyotp

# key = pyotp.random_base32()
key = "EduCodeWithKPSecretPassKey"

totp = pyotp.TOTP(key)
# TTOP is time-based, so value will NOT change based on time

print(totp.now())

# time.sleep(30)
# print(totp.now())

input_code = input("Enter 2FA Code:")

# code = totp.now()
# print(input_code == code)
if (totp.verify(input_code)):
    print(f"Correct!")
else:
    print("That is NOT correct")