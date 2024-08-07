#!/usr/bin/python3
"""
This function prints the Pascals Triangle of equivalent 
integer passed to it.
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Build the triangle row by row
    for i in range(1, n):
        # Start each row with a '1'
        row = [1]
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with a '1'
        row.append(1)
        triangle.append(row)

    return triangle
