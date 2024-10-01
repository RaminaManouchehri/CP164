"""
-------------------------------------------------------
Assignment 8, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-27"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
from BST_linked import BST
from functions import do_comparisons, comparison_total, letter_table
SEP = '-' * 60
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"
bst1 = BST()
bst2 = BST()
bst3 = BST()
for i in DATA1:
    i = Letter(i)
    bst1.insert(i)

for i in DATA2:
    i = Letter(i)
    bst2.insert(i)

for i in DATA3:
    i = Letter(i)
    bst3.insert(i)
fv = open('gibbon.txt', 'r')
do_comparisons(fv, bst1)
total = comparison_total(bst1)
print('Comparing by order: {}'.format(DATA1))
print('Total Comparisons: {:,}'.format(total))
print(SEP)
fv = open('gibbon.txt', 'r')
do_comparisons(fv, bst2)
total2 = comparison_total(bst2)
print('Comparing by order: {}'.format(DATA2))
print('Total Comparisons: {:,}'.format(total2))
print(SEP)
fv = open('gibbon.txt', 'r')
do_comparisons(fv, bst3)
total3 = comparison_total(bst3)
print('Comparing by order: {}'.format(DATA3))
print('Total Comparisons: {:,}'.format(total3))
print(SEP)
letter_table(bst1)
letter_table(bst2)
letter_table(bst3)