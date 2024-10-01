"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
d = Deque()
d.insert_front(363)
d.insert_front(353)
d.insert_front(3443)
d.insert_front(3)
d.insert_rear(33)
d1 = Deque()
d1.insert_front(3)
d1.insert_front(32)
d1.insert_front(1)
d1.insert_front(4)
d1.insert_rear(33)
for i in d1:
    print(i)