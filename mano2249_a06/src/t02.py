"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue
# Constants

queue = Priority_Queue()
queue.insert(2)
queue.insert(54)
queue.insert(22)
queue.insert(211)
queue.insert(5)
queue2 = Priority_Queue()
queue2.insert(677)
queue2.insert(8)
queue2.insert(2)
queue2.insert(8)
target = Priority_Queue()
target.combine(queue, queue2)

for v in target:
    print(v)