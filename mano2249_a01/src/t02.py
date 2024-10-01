"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants
fv = open("addresses.txt", "r", encoding="utf-8")
u, l, d, w, r = file_analyze(fv)
fv.close()
print(u, l, d, w, r)