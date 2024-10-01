"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genres
from Movie_utilities import read_movies
# Constants
genres = [4,3]
fv = open("movies.txt", 'r')
movies = read_movies(fv)
gmovies = get_by_genres(movies, genres)
for i in gmovies:
    print(i)
    print()