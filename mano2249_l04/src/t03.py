"""
-------------------------------------------------------
Lab 4, Task 3
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
lst = [44, 55, 11, 33, 22]
while len(lst) != 0:
    source.append(lst.pop())
for i in source:
    print(i)
print(f'insert 66')
source.insert(1, 66)
for i in source:
    print(i)
print(f'remove 11')
source.remove(11)
for i in source:
    print(i)