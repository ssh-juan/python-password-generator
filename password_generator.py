#Final Project Day 5 - Password Generator
#15nd October 2024
#Her link: https://appbrewery.github.io/python-day5-demo

#Hard Level
#Generates the password that doesn't follow a pattern.

import random
import string

print("Welcome to Juan's PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for letter in range(nr_letters):
    password += random.choice(string.ascii_letters)

for symbol in range(nr_symbols):
    password += random.choice(string.punctuation)

for num in range(nr_numbers):
    password += str(random.randint(0,9))

print(f"The password is: {password}")

####################################################

# Converte a string para uma lista de caracteres
password_list = list(password)

# Embaralha a lista
random.shuffle(password_list)

# Converte a lista embaralhada de volta para uma string
password = ''.join(password_list)

print(f"The shuffled password is: {password}")