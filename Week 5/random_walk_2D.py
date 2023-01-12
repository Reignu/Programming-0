# ---
# SCRIPT NAME: 
#   <random_walk_1D.py>
#
# DESCRIPTION:
# Creates a random 2D walk, with 'wrapped' (or 'periodic')
# boundaries in x and y.
#

import random
import time
import sys

# Return a string representation of a list
def graphics(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = '')
        print("")

# Return an 'empty' string with a symbol at position
def create_grid(empty, size):
    lsts = []
    for i in range(size):
        for j in range(size):
            lst = [empty] * size
        lsts.append(lst)
    return lsts

# Move a position randomly inside a von Neumann neighbourhood
# wrapping the move at the edges with the % operator   
def von_neumann_move(position, size):
    i = position[0]; j = position[1]
    offsets = [[-1, 0],[0, 1],[1, 0],[0, -1]]
    sample = random.randint(0, 3)
    i += offsets[sample][0]; j += offsets[sample][1]; 
    return [i % size, j  % size]
    
    
# ----------------------------
SIZE = 40
WALKS = 100
TRIALS = 500
EMPTY_GRAPHIC = "#"
PARTICLE_GRAPHIC = " "

for w in range(WALKS):
    grid = create_grid(EMPTY_GRAPHIC, SIZE)
    origin = int(SIZE * 0.5)
    position = list([origin, origin])
    grid[position[0]][position[1]] = PARTICLE_GRAPHIC
    print(grid)
    print(position) 
    for t in range(TRIALS):
        position = von_neumann_move(position, SIZE)
        grid[position[0]][position[1]] = PARTICLE_GRAPHIC
        print(f"time({t}), walk({w})")
        graphics(grid)
        time.sleep(0.02)