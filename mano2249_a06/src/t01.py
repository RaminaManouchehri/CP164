"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants
source = Queue()
source.insert(1)
source.insert(3)
source.insert(5)
source.insert(7)
source.insert(9)

source1 = Queue()
source1.insert(1)
source1.insert(3)
source1.insert(5)
source1.insert(7)
source1.insert(9)

source2 = Queue()
"""
source2.insert(2)
source2.insert(4)
source2.insert(6)
source2.insert(8)
source2.insert(10)
"""

target = Queue()
"""
target.insert(11)
target.insert(22)
target.insert(33)
target.insert(44)
"""
#target._append_queue(source)
#target._move_front_to_rear(source)
"""
target.combine(source1, source2)
for i in target:
    print(i)
"""
"""
target1, target2 = source.split_alt()
for v in target1:
    print('target1 {}'.format(v))
print()
for v in target2:
    print('target2 {}'.format(v))
"""
equals = source == source1
print(equals)