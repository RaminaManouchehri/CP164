"""
-------------------------------------------------------
Lab 10, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts
from test_Sorts_array import create_sorted, create_randoms, create_reversed, test_sort
# Constants

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")
title = 'Shell Sort'
func = Sorts.insertion_sort
test_sort(title, func)
