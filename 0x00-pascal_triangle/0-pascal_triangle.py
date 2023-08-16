#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []

    # Initialize the result list with the first row list
    result = [[1]]

    for i in range(1, n):
        # Calculate the next row
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)


        # Append the row to the result list
        result.append(row)


    return result

