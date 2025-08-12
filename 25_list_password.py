# Simple Password Generator: Generate a random password with specified length using letters, numbers, and symbols.

import random
import string

print("Generate a random password with specified length using letters, numbers, and symbols")

length = int(input("Enter password length: "))

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Your random password is:", generate_password(length))
