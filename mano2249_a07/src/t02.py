"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-04-08"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List
from List_linked import List
list1 = List()
list2 = List()
list3 = List()
list1.append(22)
list1.append(33)
list1.append(11)
list1.append(55)
list1.append(44)
list2.append(2)
list2.append(4)
list2.append(6)
list2.append(8)
"""
list2.insert(5)
list2.insert(0)
list2.insert(12)
list2.insert(43)
list1.clean_r()
for i in list1:
    print(i)
print()
for i in list2:
    print(i)
#equals = list1 == list2
"""
value = list1.remove(44)
print("c", value)
for i in list1:
    print(i)
previous, current, index = list1._linear_search(99)
print(previous)
print(current)
print(index)
#list3.union(list1, list2)
list3.combine_r(list1, list2)
for i in list3:
    print(i)

