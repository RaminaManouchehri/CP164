"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-01"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
pq = Priority_Queue()
value = 5
# Constants
pq.insert(value) 
value = 17
pq.insert(value) 
for i in pq:
    print(i)
    
v = pq.peek()
print(v)
