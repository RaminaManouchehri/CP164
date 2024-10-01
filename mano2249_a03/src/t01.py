"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from functions import stack_split_alt
from Stack_array import Stack
# Constants
source = Stack()
source.push(5)
source.push(7)
source.push(8)
source.push(9)
source.push(12)
source.push(14)
source.push(8)
print("Source")
for i in source:
    print(i)

print("Target1")

target1, target2 = stack_split_alt(source)
for i in target1:
    print(i)
    
print("Target2")

for i in target2:
    print(i)

print("source")

for i in source:
    print(i)