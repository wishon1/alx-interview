#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    """
    Generates Pascal's triangle with 'n' rows.
    Args:
    - n: The number of rows in the Pascal's triangle. Must be a
         positive integer.

    Returns:
    - A list of lists representing Pascal's triangle with 'n' rows.
    """
    if n <= 0:
        return []  # Return an empty list when n is less than or equal to 0

    tri = []  # Initialize an empty list to store the Pascal's triangle

    for rowNumber in range(n):
        # Initialize the current row with 1s
        row = [1] * (rowNumber + 1)

        # Loop over each element of the current row except the first and last
        for innerIndex in range(1, rowNumber):
            # Calculate the value of the current element using the values
            # from the previous row
            row[innerIndex] = tri[rowNumber - 1][innerIndex - 1]\
                + tri[rowNumber - 1][innerIndex]

        # Append the current row to the triangle list
        tri.append(row)

    return tri
