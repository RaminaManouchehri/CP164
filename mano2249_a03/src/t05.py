"""
-------------------------------------------------------
Assignment 3, Task 5
"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
# Constants
maze = {'Start': ['A'], 'A':[]}
    

path = stack_maze(maze)
print(path)