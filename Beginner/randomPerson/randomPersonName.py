"""
## Project Name
Generate Random Person Name

## Project Description
Create a program that reads a list of names from a text file, randomly picks one, and displays it. 
It's perfect for practicing file handling and working with lists in Python.

## Learning Benefits
This project is about reading text from files, processing text data, and applying the random.choice() function on lists, 
all while building a program that’s both useful and easy to expand.

## Prerequisites
Required Libraries: random
You don’t need to install any libraries since random is a standard library.
Required Files: Download the text file in this link.
IDE: You can use any IDE on your computer to code the project.

"""


import random

# Open the file in read mode
file = open("names.txt", "r")
# Read the entire content of the file and split into lines
names = file.read().splitlines()

print("random selected name is:", random.choice(names))

file.close()