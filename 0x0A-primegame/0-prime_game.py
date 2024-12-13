#!/usr/bin/python3
""" This module
    contains the function isWinner.
"""


def isWinner(x, nums):
    """ Determine the winner of the game based on the number
    of prime numbers in the list of numbers.
    Args:
        x (int): The number of rounds.
        nums (list): The list of numbers.
    Returns:
        str: The winner of the game.
        """
    if not nums or x < 1:
        return None

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def prime_count(n):
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count(n) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
