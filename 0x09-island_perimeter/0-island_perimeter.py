#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    island_perimeter - Function that returns the perimeter
    of the island described in grid list
    Args:
        grid (list): List of list of integers
    Returns:
        int: Perimeter of the island
    """
    number_of_boxes = 0
    shared_sides = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                number_of_boxes += 1
                # Check above
                if i > 0 and grid[i - 1][j] == 1:
                    shared_sides += 1
                # Check left
                if j > 0 and grid[i][j - 1] == 1:
                    shared_sides += 1

    return (number_of_boxes * 4 - shared_sides * 2)
