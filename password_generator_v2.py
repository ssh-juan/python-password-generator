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

password_list = []

for letter in range(nr_letters):
    password_list.append(random.choice(string.ascii_letters))

for symbol in range(nr_symbols):
    password_list.append(random.choice(string.punctuation))

for num in range(nr_numbers):
    password_list.append(random.randint(0,9))

#Checking the list
print(password_list)

# Shuffling the list
random.shuffle(password_list)

#Checking the shuffled list
print(password_list)

#Making the password variable
password = ""
for pwd in password_list:
    password += str(pwd)

print(f"The password is: {password}")