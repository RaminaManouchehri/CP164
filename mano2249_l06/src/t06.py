"""
-------------------------------------------------------
Lab 6, Task 6
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list, list_to_array
from List_array import List

source = [5,4,3,2,1]
llist = List()
array_to_list(llist, source)
print(source)
for v in llist:
    print(v)

list_to_array(llist, source)
print(source)
print(llist.is_empty())