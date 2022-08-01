#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            a, b = matrix[i][j], matrix[j][i]
            matrix[i][j], matrix[j][i] = b, a
    for row in matrix:
        row.reverse()

