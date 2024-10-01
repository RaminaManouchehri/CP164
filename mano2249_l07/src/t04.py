"""
-------------------------------------------------------
Lab 7, Task 4
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
lst3 = List()
array = [1, 3, 5, 7, 9]
array2 = [2, 4]
for value in array:
    lst1.append(value)
for value in array2:
    lst2.append(value)
"""
target1, target2 = lst1.split_alt()
for i in target1:
    print(i)
print()

for j in target2:
    print(j)
"""
lst3.combine(lst1, lst2)
lst1.clean()
for value in lst3:
    print(value) 
