"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
# Constants
stack = Stack()

source = [11, 22, 33, 44, 55]
array_to_stack(stack, source)
target = []
stack_to_array(stack, target)
print(target)
