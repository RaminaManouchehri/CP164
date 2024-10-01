"""
-------------------------------------------------------
Lab 7, Task 3
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
array = [11, 22, 33, 44, 55]
for value in array:
    lst.append(value)
target1, target2 = lst.split_alt_r()
print("Target1: ")
for value in target1:
    print(value)
print()
print("Target2: ")
for value in target2:
    print(value)