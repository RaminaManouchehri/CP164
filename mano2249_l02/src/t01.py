"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
stack = Stack()
# Constants

if stack.is_empty():
    print("Empty")
else:
    print("Not empty")
    
stack.push(12)
value = stack.pop()

print(f"{value} has been removed")
stack.push(44)
stack.push("dog")
print(stack.peek())
