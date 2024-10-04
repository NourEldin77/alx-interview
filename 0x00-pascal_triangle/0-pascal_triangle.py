#!/usr/bin/python3
""" Pascal's trinagle module"""


def pascal_triangle(n):
    """ return pascal's triangle of n """
    pascal_triangle = []
    if n > 0:
        for row_index in range(1, n + 1):
            current_row = []
            binomial_coeff = 1

            for col_index in range(1, row_index + 1):
                current_row.append(binomial_coeff)
                binomial_coeff = binomial_coeff * (row_index -
                                                   col_index) // col_index

            pascal_triangle.append(current_row)

    return pascal_triangle
