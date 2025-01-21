"""
Project Description
We will start this week with a small project about tuples. Your task is to write a program that takes a tuple of numbers,
 finds the second largest number, and prints out that number.

You can start your program by having this tuple as the first line:
numbers = (10, 5, 8, 20, 15)

👉 Note the difference between tuples and lists? Tuples are surrounded by round parenthesis, 
and they are immutable. Otherwise, they behave very similar.
"""

numbers = (10, 5, 8, 20, 15)
sorted_numbers = sorted(numbers)
print(sorted_numbers[-2])
