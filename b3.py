def is_safe(board, row, col, n):

    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row + 1
    j = col - 1

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


def solve(board, col, n):

    # All queens are placed
    if col == n:
        return True

    # Try every row
    for row in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 1

            # Solve next column
            if solve(board, col + 1, n):
                return True

            # Remove queen - Backtracking
            board[row][col] = 0

    return False


# Main program
n = int(input("Enter number of queens: "))

board = [[0 for _ in range(n)] for _ in range(n)]


if solve(board, 0, n):

    print("\nSolution:")

    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

else:

    print("No solution exists.")