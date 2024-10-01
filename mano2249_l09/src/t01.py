"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import read_movies
from functions import hash_table
# Constants
fv = open('movies.txt', 'r')

values = read_movies(fv)
hash_table(7, values)

fv.close()
