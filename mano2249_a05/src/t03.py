"""
-------------------------------------------------------
Simple Set testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-03-03"
-------------------------------------------------------
"""
# Imports
from set_array import Set

# Constants
SEP = "-" * 60

# Testing
source = Set()
print("Empty Set:")
source.print_set()
print(SEP)

for i in range(6):
    source.insert(i)

print("Value of _slot:")
print("Expected: 6, Actual:", source._slot)

source.print_set()
print("Values in set:")

for v in source:
    print(v)
print(SEP)

print()
print("delete 3")
deleted = source.delete(3)
print("deleted:", deleted)
print("Value of _slot:")
print("Expected: 3, Actual:", source._slot)
source.print_set()
print("Values in set:")

for v in source:
    print(v)
print(SEP)

print()
print("Test _linear_search")
print("Search 5")
i = source._linear_search(5)
print("Expected: 5, Actual:", i)
print("Search 5")
i = source._linear_search(3)
print("Expected -1, Actual", i)
print("Insert 99")
source.insert(99)
print("Value of _slot:")
print("Expected: 6, Actual:", source._slot)
print("Search 99")
i = source._linear_search(99)
print("Expected 3, Actual", i)
print(SEP)
source.print_set()

source = Set()
self = Set()
source.insert(1)
self.insert(2)
target = self.difference(source)
target.print_set()

