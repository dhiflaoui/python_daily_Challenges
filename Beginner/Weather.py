"""
Project Description

Create a program that asks the user about the current weather and, 
using a dictionary for decision-making, suggests an activity.
"""

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

# Prompt the user to choose a weather condition
print("What's the weather like today?")
print("1: Sunny and nice")
print("2: Rainy or gloomy")
print("3: Windy or chilly")
print("4: Snowy and cold")

# Get user input
user_choice = input("Enter your choice (1, 2, 3, or 4): ")

# Display the corresponding activity
if user_choice in weather_activities:
    print(weather_activities[user_choice])
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")