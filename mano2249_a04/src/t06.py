"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key
# Constants
source = Priority_Queue()
source.insert(5)
source.insert(8)
source.insert(12)
source.insert(8)
source.insert(7)
source.insert(9)
source.insert(14)
key = 9
target1, target2 = source.split_key(key)
print("Target1")
for i in target1:
    print(i)
print()
print("Target2")
for i in target2:
    print(i)
