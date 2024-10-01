"""
-------------------------------------------------------
Lab 6, Task 5
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

lst.append(22)
lst.append(33)
lst.append(11)
lst.append(55)
lst.append(44)
#print(lst.__getitem__(1))
lst.__setitem__(3,99)
#print(lst.__getitem__(1))
for i in lst:
    print(i)
