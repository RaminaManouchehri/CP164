"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-20"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants
list1 = List()
list2 = List()
list1.insert(4,1)
list1.insert(2,5)
list1.insert(1,16)
list1.insert(3,44)
list2.insert(3,5)
list2.insert(2,0)
list2.insert(1,11)
list2.insert(0,43)
for i in list1:
    print(i)
print("Target 1")
value = list1[3]
print("v", value)
target1, target2 = list1.split_alt()
for v in target1:
    print(v)
print("Target 2")
for v in target2:
    print(v)