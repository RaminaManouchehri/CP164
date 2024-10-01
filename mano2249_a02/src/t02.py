"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_rating
from Movie_utilities import read_movies
# Constants
rating = 8.1
fv = open("movies.txt", 'r')
movies = read_movies(fv)
rmovies = get_by_rating(movies, rating)
for i in rmovies:
    print(i)
    print()