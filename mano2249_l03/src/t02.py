"""
-------------------------------------------------------
Lab 3, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants
queue = Queue()
queue.insert(3)
queue.insert(2)
value = queue.remove()
print(value)
value = queue.peek()
print(value)
