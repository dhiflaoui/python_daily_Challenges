"""
## Project Description
Write a program that gently suggests self-care activities for the day. The program randomly selects an activity from a predefined list of calming, 
relaxing actions to promote mental well-being.

self_care_activities = [
    "Take a short walk in nature. 🌿",
    "Drink a big glass of water. 💧",
    "Do some deep breathing for 5 minutes. 🧘‍♂️",
    "Listen to your favorite music. 🎵",
    "Write down three things you're grateful for. ✨",
    "Read a chapter from a book you love. 📚",
    "Stretch your body gently. 🤸‍♀️",
    "Spend a few minutes with a pet or a loved one. 🐾",
    "Watch the sunset or sunrise. 🌅"
]

## How the Program Works
Any time you run the program, it generates a self-care suggestion you can do at some point in your day.


## Prerequisites
Required Libraries: random library (it comes preinstalled with Python)
Required Files: No files are needed for this project.
IDE: You can use any IDE on your computer to code the project.
"""

self_care_activities = [
    "Take a short walk in nature. 🌿",
    "Drink a big glass of water. 💧",
    "Do some deep breathing for 5 minutes. 🧘‍♂️",
    "Listen to your favorite music. 🎵",
    "Write down three things you're grateful for. ✨",
    "Read a chapter from a book you love. 📚",
    "Stretch your body gently. 🤸‍♀️",
    "Spend a few minutes with a pet or a loved one. 🐾",
    "Watch the sunset or sunrise. 🌅"
]
import random
print("hello ! here 's your self-care suggestion for today:")
print(random.choice(self_care_activities))
print("Remember, you are doing great!")