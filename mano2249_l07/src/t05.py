"""
-------------------------------------------------------
Lab 7, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from List_linked import List
lst1 = List()
lst2 = List()
lst3 = List()
array = [22, 33, 11, 55]
array2 = [11, 55, 44]
for value in array:
    lst1.append(value)
for value in array2:
    lst2.append(value)
lst3.union_r(lst1, lst2)
for value in lst3:
    print(value)
