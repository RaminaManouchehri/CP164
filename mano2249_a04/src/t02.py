"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants
source = Queue()
target = Queue()
source.insert(9)
source.insert(8)
source.insert(9)
target.insert(9)
target.insert(9)
target.insert(8)
equals = source == target
print(equals)
