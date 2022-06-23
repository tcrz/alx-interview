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
    keys = [0]
    for i in boxes[0]:
        keys.append(i)

    lockedboxes = []
    indexList = [boxes.index(i) for i in boxes]
    print(indexList)

    for i in range(len(boxes)):
        if i in keys:
            for k in boxes[i]:
                keys.append(k)
        else:
            lockedboxes.append(i)

    for i in lockedboxes:
        if i in keys:
            for k in boxes[i]:
                keys.append(k)
    print(list(set(keys)))

    # for i in range(len(boxes)):
    #     if i not in keys:
    #         return False

    if indexList != list(set(keys)):
        return False
    return True
