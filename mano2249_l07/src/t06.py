"""
-------------------------------------------------------
Lab 7, Task 6
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from List_linked import List
lst = List()
array = [22, 24, 23, 25, 10]
for value in array:
    lst.append(value)
lst.reverse_r()
for value in lst:
    print(value)