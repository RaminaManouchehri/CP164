"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_BST import Hash_Set
ash = Hash_Set(20)
fv = open('gibbon.txt', 'r')
insert_words(fv, ash)
total, max_word = comparison_total(ash)
print('Using linked BST Hash_Set')
print()
print('Total Comparisons: {:,}'. format(total))
print("Word with maximum comparisons '{}': {:,}".format(
    max_word.word, max_word.comparisons))
