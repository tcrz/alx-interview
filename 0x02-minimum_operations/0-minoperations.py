#!/usr/bin/python3

def minOperations(n):
    current = 1
    num_of_val_copied = 0
    steps = 0
    while current < n:
        rest = n - current
        if (rest % current == 0):
            num_of_val_copied = current
            current += num_of_val_copied
            steps += 2
        else:
            current += num_of_val_copied
            steps += 1
    return steps
