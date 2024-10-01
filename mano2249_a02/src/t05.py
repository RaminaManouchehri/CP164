"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import genre_counts
from Movie_utilities import read_movies
# Constants

fv = open("movies.txt", 'r')
movies = read_movies(fv)
counts = genre_counts(movies)
print(counts)