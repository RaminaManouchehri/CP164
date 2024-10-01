"""
-------------------------------------------------------
Assignment 5, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-18"
-------------------------------------------------------
"""
# Imports
from List_array import List 
# Constants
"""
source = List()
source.append(11)
source.append(11)
source.append(1177)
source.append(11)
source.append(22)
source.clean()
print("cleaned source")
for i in source:
    print(i)
print()
"""
target = List()
source1 = List()
source1.append(22)
source1.append(33)
source1.append(11)
source1.append(55)
source2 = List()
source2.append(11)
source2.append(55)
source2.append(44)
target.union(source1, source2)
for i in target:
    print(i)
"""
equals = source == target
print()
print(f"equals: {equals}")
key = 2
target1, target2 = source2.split()
target1, target2 = source2.split_alt()
value = source.remove_front()
print(f"value of front: {value}")
source2.remove_many(key)
target.union(source1, source2)
for i in source2:
    print(i)
target.combine(source1, source2)
target.intersection(source1, source2)
print(f'target:')
for i in target:
    print(i)
print()
key = 22
n = source.count(key)
print(f"n = {n}")
"""
"""
for i in target2:
    print(i)
"""
