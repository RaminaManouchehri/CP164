"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_year
from Movie_utilities import read_movies
# Constants
year = 2007
fv = open("movies.txt", 'r')
movies = read_movies(fv)

ymovies = get_by_year(movies, year)
for v in ymovies:
    print(v)
    print()