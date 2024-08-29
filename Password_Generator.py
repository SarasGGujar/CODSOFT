# Password Generation Program

import random
import string

l = int(input("Enter the Length of Password: "))

up = random.choice(string.ascii_uppercase)
low = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)

b = [up, low, digit]

remaining_l = l - len(b)
b += random.choices(string.ascii_letters + string.digits, k=remaining_l)

random.shuffle(b)
password = "".join(b)

print("Your Generated password:", password)
