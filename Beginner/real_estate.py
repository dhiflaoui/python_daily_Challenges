"""
Project Description
This is a simple beginner project where the program estimates the price of a property based on the size of the house (in square feet) and its location (city or suburb). 
The program will help practice basic Python concepts such as user input, conditional statements, and basic calculations.
"""

property_size = float(input("Enter the size of the property in square feet: "))

location = input("Enter the location (city or suburb): ").lower()

if location == "city":
    price_per_sqft = 250
elif location == "suburb":
    price_per_sqft = 150
else:
    print("Invalid location entered. Please enter 'city' or 'suburb'.")
    exit()  # Exit the program if the location is invalid

estimated_price = property_size * price_per_sqft


print(f"The estimated price for {property_size} sq ft property in the city is : ${estimated_price:,.2f}")