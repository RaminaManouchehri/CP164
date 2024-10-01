"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-04-10"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts
a = Deque()
b = [3, 5699, 68, 706, 6, 77, 67, 7685]
for n in b:
    a.insert_rear(n) 
Sorts.gnome_sort(a)
print("sorted linked: {}".format([x for x in a]))