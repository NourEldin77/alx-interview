#!/usr/bin/python3
import sys


def exit_with_message(message):
    print(message)
    sys.exit(1)


def place_queens(n, row, current_positions, columns, diagonals1, diagonals2, results):
    if row == n:
        results.append([[i, current_positions[i]] for i in range(n)])
        return

    for col in range(n):
        if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
            continue

        current_positions[row] = col
        columns.add(col)
        diagonals1.add(row - col)
        diagonals2.add(row + col)

        place_queens(n, row + 1, current_positions, columns,
                     diagonals1, diagonals2, results)

        current_positions[row] = -1
        columns.remove(col)
        diagonals1.remove(row - col)
        diagonals2.remove(row + col)


def main():
    if len(sys.argv) != 2:
        exit_with_message("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        exit_with_message("N must be a number")

    if n < 4:
        exit_with_message("N must be at least 4")

    results = []
    current_positions = [-1] * n
    columns = set()
    diagonals1 = set()
    diagonals2 = set()

    place_queens(n, 0, current_positions, columns,
                 diagonals1, diagonals2, results)

    for solution in results:
        print(solution)


if __name__ == "__main__":
    main()
