def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # The position is safe
    return True


def solve_n_queens(board, col, N):
    # Base case: all queens have been placed
    if col == N:
        return True

    # Try placing the queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen in the current position
            board[i][col] = 1

            # Recursively place the remaining queens
            if solve_n_queens(board, col + 1, N):
                return True

            # Backtrack: remove the queen from the current position
            board[i][col] = 0

    # Could not find a safe position for the queen in the current column
    return False


def print_board(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Driver code
N = int(input("Enter the number of queens: "))
board = [[0 for i in range(N)] for j in range(N)]

if solve_n_queens(board, 0, N):
    print_board(board)
else:
    print("Solution does not exist")