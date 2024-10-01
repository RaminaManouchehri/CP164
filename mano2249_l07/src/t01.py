"""
-------------------------------------------------------
Lab 7, Task 1
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
previous, current, index = lst._linear_search_r(23)
print(previous._value)
print(current._value)
print(index)
"""
value = lst.remove(23)
print(value)
"""