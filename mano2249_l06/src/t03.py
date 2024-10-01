"""
-------------------------------------------------------
Lab 6, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()
lst.insert(0,0)

lst.append(5)
lst.append(8)
lst.append(7)
lst.insert(-1,3)
#lst.remove(3)
for v in lst:
    print(v)