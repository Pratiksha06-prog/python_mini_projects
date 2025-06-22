#Random Password Genrator

import random
import string

length = int(input("Enter the lenght of the password:"))

use_letter = input("Include letter? (y/n): ").lower() == 'y'
use_digit = input("Include digit? (y/n): ").lower() == 'y'
use_symbols = input("Include sumbols? (y/n)").lower() == 'y'

characters = " " 

if use_letter:
    characters += string.ascii_letters

if use_digit:
    characters +=  string.digits

if use_symbols:
    characters += string.punctuation      

if not characters:
    print("You must choose at least one character!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nYour generated password is: {password}")