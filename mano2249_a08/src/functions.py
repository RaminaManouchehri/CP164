"""
-------------------------------------------------------
Functions
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
# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"
bst1 = BST()
bst2 = BST()
bst3 = BST()
for i in DATA1:
    l = Letter(i)
    bst1.insert(l)
for i in DATA2:
    l = Letter(i)
    bst2.insert(l)
for i in DATA3:
    l = Letter(i)
    bst3.insert(l)
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # your code here
    for v in file_variable:
            for letter in v:
                if letter.isalpha():
                    var = Letter(letter.upper())
                    bst.retrieve(var)
    return
def comparison_total(bst):

        """

        -------------------------------------------------------

        Sums the comparison values of all Letter objects in bst.

        Use: total = comparison_total(bst)

        -------------------------------------------------------

        Parameters:

            bst - a binary search tree of Letter objects (BST)

        Returns:

            total - the total of all comparison fields in the bst

                Letter objects (int)

        -------------------------------------------------------

        """

        a = bst.inorder()

        total = 0

        for letter in a:

            total+=letter.comparisons

        return total

def letter_table(bst):

    """

    -------------------------------------------------------

    Prints a table of letter counts for each Letter object in bst.

    Use: letter_table(bst)

    -------------------------------------------------------

    Parameters:

        bst - a binary search tree of Letter objects (BST)

    Returns:

        None

    -------------------------------------------------------

    """

    total = comparison_total(bst)

    print('Letter Count/Percent Table')

    print()

    print('Total Count: {:,}'.format(total))

    print()

    print('Letter  Count       %')

    print('---------------------')

    a = bst.inorder()

    for v in a:

        print('    {}  {}   {:.2f}%'.format(v.letter, v.comparisons, (v.comparisons / total) * 100))

    return