#!/usr/bin/python3
"""method that determines if a given data set represents
a valid UTF-8 encoding"""


def validUTF8(data):
    n_bytes = 0

    for num in data:
        binary = format(num, "#010b")[2:]
        if n_bytes == 0:
            for bit in binary:
                if bit == '0':
                    break
                n_bytes += 1
        else:
            if binary[0] == '0' or binary[1] == '1':
                return False

            n_bytes -= 1
        return n_bytes == 0
