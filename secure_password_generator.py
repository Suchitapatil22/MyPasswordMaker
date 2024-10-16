import random
import string

pass_len = 15
allchars = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range (pass_len):
    password = password + random.choice(allchars)

print("Your Secure Password is: ", password)

