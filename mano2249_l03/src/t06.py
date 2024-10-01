"""
-------------------------------------------------------
Lab 3, Task 6
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-01"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
pq = Priority_Queue()
# Constants
source = [11, 22, 33, 44]
array_to_pq(pq, source)
print()

target = []
pq.insert(12)
pq.insert(1)
pq.insert(3)
pq.insert(4)
pq_to_array(pq, target)
print(target)
print()

a = [11, 22, 33, 44]

priority_queue_test(a)
 