"""
-------------------------------------------------------
Lab 9, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Movie_utilities import read_movies
fv = open('movies.txt', 'r')
hs = Hash_Set(7)
a = read_movies(fv)
for i in a:
    hs.insert(i)
hs.debug()
fv.close()