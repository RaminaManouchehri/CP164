"""
-------------------------------------------------------
Lab 3, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test
# Constants
source = [11, 22, 33, 44]
queue = Queue()
array_to_queue(queue, source)
print(source)
for i in queue:
    print(i)

print()

target = []
queue_to_array(queue, target)
print(f'target: {target}')
for i in queue:
    print(i)
print()
    
a = [11, 22, 33, 44]

queue_test(a)
