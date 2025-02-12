"""
## Project Name 
Generate Text Files with Random Names

## Project Description

Your task for today is to create a Python program which generates a new text file every time you run it.

## How the Project Works
When you run the program, it should generate a new text file. 
The program assigns a random name of 10 characters to the text file and also writes that random text inside the text file as content.

## Prerequisites

Required Libraries: string, random
Required Files: No files are required.
IDE: You can use any IDE on your computer to code the project.
"""
import string
import random
# Define the characters to be used for the random name
characters = string.ascii_letters + string.digits
print(characters)
# Generate a random name of 10 characters
random_name = ''.join(random.choice(characters) for _ in range(10))
# Create a new text file with the random name
# f = open(random_name + ".txt", "w")
# f.write(random_name)
# f.close()