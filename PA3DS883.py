# Shahriyar Mammadli
# LeetCode problem '883. Projection Area of 3D Shapes' solution
# Import required libraries
import numpy as np

def projectionArea(grid):
    xy = 0
    # Projection area in the xy plane is the sum the cells that has an cube in it
    for cell in grid:
        for val in cell:
            if(val > 0):
                xy = xy + 1
    # Projection area in the xz plane is the sum of maximum values in each row
    xz = sum(np.max(grid, 1))
    # Projection area in the xz plane is the sum of maximum values in each column
    yz = sum(np.max(grid, 0))
    return xy + xz + yz

print(projectionArea([[1,2],[3,4]]))