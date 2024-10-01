"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-08"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants
source = List()
lst = [44, 55, 11, 33, 22, 11]
while len(lst) != 0:
    source.append(lst.pop())

value = source[4]
print(value)
print()


source[2] = value
for i in source:
    print(i)
