#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer
"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []
    # First row/list of the triangle
    final_list = [[1]]
    # Loop the number of additional rows/lists needed.
    # First list already added, number of new lists needed is n - 1
    for x in range(n-1):
        # Add zeros at the beginning and ending of last sublist in
        # final_list(makes for easier addition for where values
        # are non-existent)
        temp = [0] + final_list[-1] + [0]
        # Next list to be added to final_list
        new_list = []
        # Length of the next row (length of the last sublist + 1)
        for y in range(len(final_list[-1]) + 1):
            # Necessary addition on values of current row/list and
            # appended to next list/row
            new_list.append(temp[y] + temp[y+1])
        # Append new row to final_list
        final_list.append(new_list)
    return final_list
