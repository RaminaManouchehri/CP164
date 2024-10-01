"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
# Constants
source = Queue()
target = Queue()

for i in range(0,9):
    source.insert(i)
    
empty = source.is_empty()
print(f"Empty: {empty} ?")

full = source.is_full()
print(f"Full: {full} ?")

length = len(source)
print(f"Length: {length} ?")

for i in range(0,8):
    target.insert(i) 
equals = source == target
print(f"Equal: {equals} ?")

remove = source.remove()
print(f"Remove: {remove} ?")

peek = source.peek()
print(f"Peek: {peek} ?")


