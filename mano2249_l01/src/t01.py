"""
-------------------------------------------------------
Lab 1, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-18"
-------------------------------------------------------
"""
# Imports

# Constants
from Movie import Movie
from Stack_linked import Stack
"""
object = Movie('T1', 2000, 'D1', 5, [3, 4, 5, 8])
print(object.genres_string())
"""
target = Stack()
source = Stack()
source.push(11)
source.push(2)
"""
source.push(119)
source.push(9)

for i in source:
    print(i)
source.reverse()
for i in source:
    print(i)
"""
target._move_top(source)
target._move_top(source)
for i in target:
    print(i)