"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from functions import queue_combine
from Queue_array import Queue
# Constants
source1 = Queue()
source1.insert(5)
source1.insert(8)
source1.insert(12)
source1.insert(8)
source2 = Queue()
source2.insert(7)
source2.insert(9)
source2.insert(14)
target = queue_combine(source1, source2)

for i in target:
    print(i)