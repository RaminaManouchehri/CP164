"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-27"
-------------------------------------------------------
"""
# Imports

# Constants

from BST_linked import BST

bst = BST()
bst2 = BST()
bst.insert(3)
bst.insert(1)
bst.insert(5)
bst.insert(0)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(-1)
bst.insert(-2)
bst.insert(-0.5)
bst.insert(-3)
bst.insert(-1.5)
bst.insert(9)
bst.insert(10)


#bst.remove(11)
"""
for i in bst:
    print('{},'.format(i))
"""
value = bst.min_r()
value = bst.max_r()
a = bst.levelorder()
count = bst.leaf_count()
count = bst.two_child_count()
count = bst.one_child_count()
parent = bst.parent(1)
value = bst.parent_r(900)

print()
for i in a:
    print(i)
equals = bst == bst2
b = bst.is_valid()
b = 900 in bst
count = bst.two_child_count()
count = bst.one_child_count()
count = bst.leaf_count()
zero, one, two = bst.node_counts()
#value = bst.parent()
print(f'z:{zero}, one:{one}, t:{two}')
v = bst.retrieve_r(6)
print("v", v)