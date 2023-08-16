#!/usr/bin/python3
def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle

    parameters:
         n [int]:
            the number of rows of Pascal's triangle to recreate

    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    result = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)

    result.append(row)

    return result
