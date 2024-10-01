"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
# Constants
def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for i in values:
        h = hash(i)
        sslot = h % slots
        movie_n = i.title
        year = i.year
        print(f"{h:8d} {sslot:4d} {movie_n}, {year}")
    return