
def is_safe(board, row, col, n):

    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row + 1, col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, n):

    if col == n:
        return True

    for row in range(n):

        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter number of queens: "))
board = [[0] * n for _ in range(n)]

if solve(board, 0, n):
    print("\nSolution")
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
else:
    print("No solution exists.")
