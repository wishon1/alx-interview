#!/usr/bin/python3
"""N queens solver."""
import sys


def print_usage():
    """Print the usage message if incorrect number of arguments."""
    print("Usage: nqueens N")
    exit(1)


def validate_input(argv):
    """Validate command line input for the correct conditions.

    - Ensure only one argument is passed
    - Check if the argument is a digit
    - Ensure the argument is at least 4
    """
    if len(argv) != 2:
        print_usage()
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    return n


def solve_nqueens(n):
    """Solve the N queens problem using backtracking.

    - Use a recursive generator to find all valid solutions
    - Each solution is formatted and returned as a list of positions
    """

    def queens(n, i=0, a=[], b=[], c=[]):
        """
        Recursive generator to place queens on the board.

        - `n`: size of the board (NxN)
        - `i`: current row
        - `a`, `b`, `c`: lists to keep track of columns and diagonals that are
            under attack
        """
        if i < n:
            for j in range(n):
                if j not in a and i + j not in b and i - j not in c:
                    yield from queens(n, i + 1, a + [j], b + [i + j],
                                      c + [i - j])
        else:
            yield a

    solutions = []
    for solution in queens(n):
        formatted_solution = []
        for i, col in enumerate(solution):
            formatted_solution.append([i, col])
        solutions.append(formatted_solution)
    return solutions


def main():
    """Main function to control the flow of the program."""
    n = validate_input(sys.argv)
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
