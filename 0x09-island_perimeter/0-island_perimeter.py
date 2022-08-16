#!/usr/bin/python3
"""
Island Perimeter: returns the perimeter of the island
"""


def island_perimeter(grid):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                result += 4
                if i > 0 and grid[i-1][j] == 1:
                    result -= 2
                if j > 0 and grid[i][j-1] == 1:
                    result -= 2
    return result
