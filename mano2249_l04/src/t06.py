"""
-------------------------------------------------------
Lab 4, Task 6
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List
# Constants
source = [55, 44, 33, 22, 11]
llist = List()
array_to_list(llist, source)
print(f"List array contents")
for i in llist:
    print(i)
print()
target = []
list_to_array(llist, target)
print(f"Target contents")
for i in target:
    print(i)
