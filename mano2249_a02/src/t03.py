"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genre
from Movie_utilities import read_movies
# Constants
genre = 8
fv = open("movies.txt", 'r')
movies = read_movies(fv)
gmovies = get_by_genre(movies, genre)
for i in gmovies:
    print(i)
    print()