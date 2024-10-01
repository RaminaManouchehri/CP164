"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import random
from List_linked import List
from List_linked import _List_Node
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE):
        values.append(Number(i))
        
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = []
    for i in range(TESTS):
        lists.append(List())
    for lst in lists:
        for j in range(SIZE):
            lst.insert(0, Number(random.randrange(XRANGE)))

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    sorted = create_sorted()
    reversed = create_reversed()
    randoms = create_randoms()
    
    Number.comparisons = 0
    Sorts.swaps = 0
    func(sorted)
    sorted_comparisons = Number.comparisons
    sorted_swaps = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    func(reversed)
    reversed_comparisons = Number.comparisons
    reversed_swaps = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    arrays = create_randoms()
    for a in arrays:
        func(a)
    random_comparisons = Number.comparisons // TESTS
    random_swaps = Sorts.swaps // TESTS
    """
    
    print("n:   100       |      Comparisons       | |         Swaps          |")
    print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
    print("-------------- -------- -------- -------- -------- -------- --------")
    """
    print(f"{title:<14s}{sorted_comparisons:9.0f}{reversed_comparisons:9.0f}{random_comparisons:9.0f}{sorted_swaps:9.0f}{reversed_swaps:9.0f}{random_swaps:9.0f}")
    return


    return

