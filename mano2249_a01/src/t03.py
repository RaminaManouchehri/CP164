"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""
from functions import find_subs
string = "It was a really, really, big assignment."
sub = "real"
locations = find_subs(string, sub)
print(locations)