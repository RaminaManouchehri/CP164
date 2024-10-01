"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
source1 = Stack()
source2 = Stack()
target = Stack()
source2.push(44)
source2.push(33)
source2.push(22)
source2.push(11)
for i in source2:
    print(i)
print("L")
target.combine(source1, source2)
for i in target:
    print(i)
