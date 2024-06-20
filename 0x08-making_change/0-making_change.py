#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total using greedy method
"""

def makeChange(coins, total):
    """ Return the fewest number of coins needed to meet total using a greedy method """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    # If we are left with an amount that is not zero,
    # we cannot make the total with the given coins
    return count if total == 0 else -1
