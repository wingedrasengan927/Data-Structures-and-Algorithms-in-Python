'''
Reference: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/
Place N Queens in a board of size N x N such that all queens are safe.
A queen can attack diagonally, row wise or column wise
'''


# Write your code here
N = int(input())
board = [[0 for x in range(N)] for y in range(N)]

def is_attacked(x, y, board):
    '''returns True is a cell is under attack
    Time Complexity - 2(1 + sqrt(2)n - O(n))'''
    # check row
    for i in range(len(board)):
        if board[x][i] == 1:
            return True
    # check columns
    for i in range(len(board)):
        if board[i][y] == 1:
            return True

    # check diagonal

    # top right
    p, q = x-1, y+1
    while p >= 0 and q < len(board):
        if board[p][q] == 1:
            return True
        p -= 1
        q += 1
    # top left
    p, q = x-1, y-1
    while p >= 0 and q >= 0:
        if board[p][q] == 1:
            return True
        p -= 1
        q -= 1
    # bottom left
    p, q = x+1, y-1
    while p < len(board) and q >= 0:
        if board[p][q] == 1:
            return True
        p += 1
        q -= 1
    # bottom right
    p, q = x+1, y+1
    while p < len(board) and q < len(board):
        if board[p][q] == 1:
            return True
        p += 1
        q += 1

    return False

def NQueens(board, N):
    if N == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if is_attacked(i, j, board):
                continue
            board[i][j] = 1
            if NQueens(board, N-1):
                return True
            board[i][j] = 0
    return False

result = NQueens(board, N)
if result:
    print("YES")
else:
    print("NO")
if result:
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end="")
        print() 