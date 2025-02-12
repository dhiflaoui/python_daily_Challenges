"""
Project Description
Choosing a movie to watch can be a struggle, especially with so many options available. In this project, 
you’ll create a simple Python program that suggests a random movie based on the genre the user selects. The program will use a predefined dictionary of movies and genres, 
allowing users to get a quick recommendation without endless scrolling.

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}
Expected Output
The program displays some initial message (i.e., Welcome to the Movie Night…) and then prompts the user to enter a genre.
 The user has entered “Drama” in the following example, so the program has selected a random movie from the “Drama” category (i.e., The Green Mile).


Prerequisites
Required Libraries: datetime, random
You don’t need to install any libraries.
Required Files: No files are needed for this project.
IDE: You can use any IDE on your computer to code the project.
"""

import random

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

print("Welcome to the Movie Night Recommender!")
genre_list = ", ".join(movies.keys())
print("Available genres are: ", genre_list)
genre = input("Enter a genre: ").capitalize()
if genre in movies:
    movie = random.choice(movies[genre])
    print(f"You should watch '{movie}'!")
else:
    print("Sorry, we don't have recommendations for that genre.")

