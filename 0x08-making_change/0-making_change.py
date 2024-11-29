#!/usr/bin/python3
""" solving a problem"""


def makeChange(coins, total):
    """
    Returns the minimum number of coins needed to make the given total.
    If the total cannot be made with the given coins, returns -1.
    """
    if total < 0:
        return 0

    number_of_change = 0
    change_arr = sorted(coins.copy(), reverse=True)
    total_cpy = total

    while total_cpy > 0 and change_arr:
        biggest_change = change_arr.pop(0)
        res = total_cpy // biggest_change
        if res > 0:
            total_cpy -= res * biggest_change
            number_of_change += res

    if total_cpy != 0:
        return -1
    return number_of_change
