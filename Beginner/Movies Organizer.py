# Create a predefined list of favorite movies
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Add a new movie to the list
new_movie = "Avengers: Endgame"
favorite_movies.append(new_movie)
print(f"'{new_movie}' has been added to your favorite movies list.")

# Remove a specific movie from the list
movie_to_remove = "The Matrix"
if movie_to_remove in favorite_movies:
    favorite_movies.remove(movie_to_remove)
    print(f"'{movie_to_remove}' has been removed from your favorite movies list.")
else:
    print(f"'{movie_to_remove}' is not in the list.")


print(f"\nTotal number of movies in the list: {len(favorite_movies)}")


print("\nMovies in alphabetical order:")
for movie in sorted(favorite_movies):
    print(movie)
