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
    unlockedKeys = [0]
    indexList = [boxes.index(i) for i in boxes]
    for box in boxes:
        for key in box:
            for i in range(len(boxes)):
                if box != boxes[i] and key == i:
                    unlockedKeys.append(key)
    if indexList == list(set(unlockedKeys)):
        return True
    return False
