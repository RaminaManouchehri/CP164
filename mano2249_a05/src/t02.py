"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
# Constants
source = Sorted_List()
source.insert(4)
source.insert(10)
source.insert(6)
source.insert(6)
source.insert(88)
source.insert(0)
source.insert(11)

source2 = Sorted_List()
source2.insert(4)
source2.insert(10)
source2.insert(6)
source1 = Sorted_List()
source1.insert(4)
source1.insert(88)
source1.insert(7)
source1.insert(6)
key = 9

b = key in source
print(f"Key in source = {b}")
i = 2
value = source[i]
print(f"Value of i= {value}")
source.clean()
print("cleaned source:")
for i in source:
    print(i)
n = source.count(key)
print(f"Key in source times = {n}")
value = source.find(key)
key = 4
print(f"Value of source = {n}")
n = source.index(key)
target = Sorted_List()
target.intersection(source1, source2)
print("target intersection:")
for i in target:
    print(i)
max1 = source.max()
min1 = source.min()
print(f'max:{max1} and min:{min1}.')
peek1 = source.peek()
print(f'peek: {peek1}')
remove1 = source.remove(key)
print(f'remove: {remove1}')
remove_front = source.remove_front()
print(f'remove front: {remove_front}')
target1, target2 = source.split()
print("split target 1 and 2:")
print("Target 1:")
for i in target1:
    print(i)
print()
print("Target 2:")
for i in target2:
    print(i)
print()
source.insert(4)
source.insert(10)
source.insert(6)
source.insert(6)
source.insert(88)
source.insert(0)
source.insert(11)
target1, target2 = source.split_alt()
print("split alt target 1 and 2:")
print("Target 1:")
for i in target1:
    print(i)
print()
print("Target 2:")
for i in target2:
    print(i)
print()

target.union(source1, source2)
print("target union:")
for i in target:
    print(i)