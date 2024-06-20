#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """ Return the fewest number of coins needed to meet total """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each
    # amount up to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin and update the min_coins list
    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(min_coins[amount],
                                    min_coins[amount - coin] + 1)

    # If min_coins[total] is still float('inf'), it means we cannot make
    # the total with the given coins
    return min_coins[total] if min_coins[total] != float('inf') else -1
