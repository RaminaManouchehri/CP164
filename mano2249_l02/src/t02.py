"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# from utilities import array_to_stack
# Constants
stack = Stack()
source = [99]

array_to_stack(stack, source)
# array_to_stack(stack, source)
print(source)
while not stack.is_empty():
    value = stack.pop()
    print(value)