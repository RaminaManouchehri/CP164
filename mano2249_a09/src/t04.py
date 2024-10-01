"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
bst = BST()
bst.insert(31)
bst.insert(7)
bst.insert(65)
bst.insert(7)
bst.insert(2)
bst.insert(32)
bst.insert(98)
bst.insert(85)
yes = 7
no = 67
print(bst.node_counts())
print(yes in bst)
print(no in bst)
print(bst.parent(yes))
print(bst.parent_r(yes))