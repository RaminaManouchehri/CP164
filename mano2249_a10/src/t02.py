"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-04-10"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List
a = List()
a.append(0)
a.append(0)
Sorts.radix_sort(a)
for v in a:
    print(v)
