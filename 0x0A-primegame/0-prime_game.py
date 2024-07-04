#!/usr/bin/python3
"""0. Prime Game module"""


def isWinner(x, nums):
    """Produce the winner of a prime number game"""
    if x <= 0 or not nums:
        return None

    # Helper function to generate prime numbers using the Sieve of Eratosthenes
    def Sieve_eratosthenes(max_n):
        """Use Sieve of Eratosthenes to find prime numbers"""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, max_n + 1):
            if is_prime[i]:
                for j in range(i * 2, max_n + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(max_n + 1) if is_prime[i]]
        return primes

    # Helper function to simulate a single game
    def simulate_game(n, primes):
        """Simulate the game and determine the winner for a given n"""
        remaining_numbers = list(range(1, n + 1))
        maria_turn = True

        while True:
            # Find the smallest prime in the remaining numbers
            prime_found = False
            for prime in primes:
                if prime in remaining_numbers:
                    prime_found = True
                    break

            if not prime_found:
                return "Ben" if maria_turn else "Maria"

            # Remove the chosen prime and its multiples
            remaining_numbers = [num for num in remaining_numbers
                                 if num % prime != 0]
            maria_turn = not maria_turn

    # Initialize win counts
    maria_wins = 0
    ben_wins = 0

    # Find the maximum n to limit the prime number generation
    max_n = max(nums)

    # Generate all primes up to max_n
    primes = Sieve_eratosthenes(max_n)

    # Simulate each game and count wins
    for n in nums:
        winner = simulate_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
