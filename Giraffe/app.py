# Setting up Python
print("Hello World!")

# Variables and Data Types
print(" ----------------------  Variables and simple data types  ---------------------- ")
character_name = "Navneet Kumar"
character_age = 28.05004
is_Male: bool = True
is_Female: bool = False

if is_Male:
    print("There is a man known as " + character_name)
    print("He is " + str(character_age) + " years old.")
elif not is_Male:
    print("Not applicable")

#################### Working with Strings
print(" ----------------------  Working with Strings ---------------------- ")
# Using \
print("Navneet\nKumar")
print("Navneet\"Kumar")

# Concatenation
Phrase = "works for RBS"
print("Navneet Kumar " + Phrase)

# Change the cases to lower, upper, title
print(Phrase.lower())
print((Phrase.islower()))
print(Phrase.upper())
print(Phrase.title())

# Length of the string
print(len(Phrase))

# Substring function
print(Phrase.upper()[0 + 2])

# Find an index of character
print(Phrase.index("RBS"))
# print(Phrase.index("Rbs"))

# Replace parameter
print(Phrase.replace("RBS", "Google"))

#################### Working with numbers
print(" \n\n----------------------  Working with numbers ---------------------- ")
print(3 + 4.5)

# Modulus - Remainder Operator
print(13 % 5)

# Converted into a string
print(str(87) + " is my favourite number")

# Functions related to numbers
# Taking Absolute values
my_num = -5
print(abs(my_num))

# Exponential using Pow()
print(pow(my_num, 2))

# Maximum, Minimum, Round Function
print(max(-2,-4))
print(min(-2,0,-4))
print(round(-2.8))

from math import *
print(sqrt(256))

# User Input
name = input("Enter your name: ")
age = input("Enter you age: ")
print(type(name))
print("Hello " + name + ", Good to know you're " + age)
