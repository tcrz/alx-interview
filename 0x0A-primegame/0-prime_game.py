#!/usr/bin/python3
"""Prime Game"""


def isPrime(num):
    """returns true if prime number"""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def removeMultiples(num, num_list):
    """removes multiples of a number in a list"""
    for x in list(num_list):
        if x != num and x % num == 0:
            num_list.remove(x)
    return num_list


def isWinner(x, nums):
    """Finds the winner of Prime Game"""
    games = []
    ben = 0
    marie = 0
    if x > len(nums):
        return None

    for i in nums:
        if i == 0:
            return None
        games.append([i for i in range(1, i+1)])
    print(games)
    for i in range(x):
        count = 0
        for x in range(len(games[i])):
            if isPrime(games[i][x]):
                count += 1
        if count % 2 == 0:
            ben += 1
        else:
            marie += 1

    if marie > ben:
        return "Marie"
    elif marie < ben:
        return "Ben"
    return None
