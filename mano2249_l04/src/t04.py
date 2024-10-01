"""
-------------------------------------------------------
Lab 4, Task 4
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
index = source.index(55)
print(f'index: {index}')
find = source.find(44)
print(f'find: {find}')
b = 33 in source
print(f'contains: {b}')
count = source.count(11)
print(f'count: {count}')
min1 = source.min()
print(f'Minimum: {min1}')
max1 = source.max()
print(f'Maximum: {max1}')