"""
-------------------------------------------------------
Lab 3, Task 5
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
# Constants
value = 9
pq.insert(value) 
value = 17
pq.insert(value) 
value = 14
pq.insert(value) 
value = 18
pq.insert(value) 
value1 = pq.remove()
for i in pq:
    print(i)
print(f"Removed value: {value1}")
