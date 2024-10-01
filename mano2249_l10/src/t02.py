"""
-------------------------------------------------------
Lab 10, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-29"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts
from test_Sorts_array import create_sorted, create_randoms, create_reversed, test_sort
# Constants
title = 'Shell Sort'
func = Sorts.insertion_sort
test_sort(title, func)
