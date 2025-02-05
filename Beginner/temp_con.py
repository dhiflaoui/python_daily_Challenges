"""

Project Description
In this project, you'll create a program that converts a list of temperatures in Fahrenheit to Celsius and vice versa.

Start the program by pasting this list in the first line of your program:

temperatures_fahrenheit = [32, 50, 77, 100, 212]
The formula to convert fahrenheit to celsius is (fahrenheit - 32) * 5 / 9


"""
temperatures_fahrenheit = [32, 50, 77, 100, 212]
temperatures_celsius = [(fahrenheit - 32) * 5 / 9 for fahrenheit in temperatures_fahrenheit]
print("Fahrenheit to Celsius:")
for fahrenheit, celsius in zip(temperatures_fahrenheit, temperatures_celsius):
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
