# N Queens Problem using Backtracking

n = 4
board = [[0]*n for _ in range(n)]

def is_safe(row, col):

    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Lower diagonal
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(col):

    if col >= n:
        return True

    for i in range(n):

        if is_safe(i, col):

            board[i][col] = 1

            if solve(col + 1):
                return True

            board[i][col] = 0

    return False

solve(0)

for row in board:
    print(row)