# Create board

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):

    valid = find_empty(bo)




def find_empty(bo):
    # Check row
    for i in range(len(bo):
        if i !=



# Print board
def print_board(bo):
    # Print First line
    print("  - - - - - - - - - - - - -")

    # For each row
    for i in range(len(bo)):

        # Print bottom border every 3 rows
        if i % 3 == 0:
            print("  - - - - - - - - - - - - -")

        # Checks each column
        for j in range(len(bo)):

            # Prints side borders every 3 columns starting with the first column
            if j % 3 == 0:
                print(' | ', end="")

            # if we reach the last column
            if j == 8:
                print(str(bo[i][j]) + ' |')
            # print the current row and column
            else:
                print(str(bo[i][j]) + " ", end="")

    # Print last bottom row
    print("  - - - - - - - - - - - - -")


print_board(board)
