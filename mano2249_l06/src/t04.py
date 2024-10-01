"""
-------------------------------------------------------
Lab 6, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
# Imports
from List_linked import List
l = List()
l.append(4)
l.append(22)
l.append(33)
l.append(11)
l.append(222)
# l.remove(55)
for v in l:
    print(v)
print(l[0])
l[0] = 66
print(l[0])
key = 33

previous, current, index = l._linear_search(key)
print()
print(previous._value)
print(current._value)
print(index)
"""
previous, current, index = l._linear_search_r(key)
print()
print(previous._value)
print(current._value)
print(index)
"""
