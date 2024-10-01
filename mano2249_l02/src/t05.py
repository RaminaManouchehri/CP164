"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Movie_utilities import read_movies
# Constants

fv = open("movies.txt", 'r')
source = read_movies(fv)
stack_test(source)