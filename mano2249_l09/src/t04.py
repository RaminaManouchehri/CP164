"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
hs = Hash_Set(7)
for i in range(35):
    hs.insert(i)
hs.debug()
print()
for i in range(10):
    hs.insert(i)
print("REHASH")
hs.debug()
