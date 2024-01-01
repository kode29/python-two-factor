import time
import pyotp

# key = pyotp.random_base32()
key = "EduCodeWithKPSecretPassKey"

# HTOP is counter-based, so value will NOT change based on time

hotp = pyotp.HOTP(key)

print(hotp.at(0)) # this will be the same always
print(hotp.at(1)) # this will be different than (0), but always be the same

# time.sleep(30)
# print(totp.now())

input_code = input("Enter 2FA Code:")

# code = totp.now()
# print(input_code == code)
if (hotp.verify(input_code)):
    print(f"Correct!")
else:
    print("That is NOT correct")