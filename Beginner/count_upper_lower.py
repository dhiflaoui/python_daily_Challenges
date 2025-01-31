"""
Project Description
This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.

"""


text = "This Sentence Has Mixed CASE Letters!"


uppercase_count = 0
lowercase_count = 0


for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1


print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")