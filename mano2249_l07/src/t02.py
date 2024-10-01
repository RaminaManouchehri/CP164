"""
-------------------------------------------------------
Lab 7, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from List_linked import List
lst1 = List()
lst2 = List()
array = [22]
array2 = [22, 24, 23, 25, 10]
for value in array:
    lst1.append(value)
for value in array2:
    lst2.append(value)
#print(lst1.is_identical_r(lst2))
#lst1.insert(2, 44)
"""
previous, current, index = lst1._linear_search(20)
print(previous._value)
print(current._value)
print(index)
value = lst1.remove(22)
print("value:", value)
value = lst1[2]
print(value)
"""
previous, current, index = lst1._linear_search_r(23)
print("p", previous._value)
print("c", current._value)
print("i", index)
equals = lst1 == lst2
print("equals:", equals)
#lst1[2] = 44
for i in lst1:
    print(i)
value = lst1.max()
print("max", value)
    
b = 54 in lst1
print(b)