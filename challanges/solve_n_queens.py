def is_safe(board, row, col, n):
    # Check if queen can be placed on board

    # Check left row
    for i in range(col):
        if board[row][i]:
            return False

    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then backtrack and remove the queen
            board[i][col] = 0

    return False


def print_board(board):
    for row in board:
       print(" ".join(["Q" if cell == 1 else "." for cell in row]))


def solve_n_queens(n):
    # create board
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("No solution exists")
        return

    print_board(board)


n = 8
solve_n_queens(n)
