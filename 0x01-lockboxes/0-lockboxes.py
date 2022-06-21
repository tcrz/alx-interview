#!/usr/bin/python3

"""
Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    if (all(isinstance(i, list) for i in boxes) is False):
        return False
    # list to hold keys
    # the first item of boxes is already unlocked
    keys = [0]
    # indexes of all items in boxes
    indexList = [boxes.index(i) for i in boxes]
    # loop through boxes
    for box in boxes:
        # loop through each key in a box for later comparison
        for key in box:
            # loop through length of boxes list to compare index with key
            for i in range(len(boxes)):
                # if box is not current box and key is equal to an index in -
                # boxes list, append key to keys list
                if box != boxes[i] and key == i:
                    keys.append(key)
    # check if indexList is equal to unique list of keys, if true,
    # all keys have been found and  all boxes can be opened
    if indexList == list(set(keys)):
        return True
    return False
