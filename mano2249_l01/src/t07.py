"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
# Constants
fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()
print(movies)
