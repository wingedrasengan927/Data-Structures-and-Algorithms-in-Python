'''
Reference: https://brilliant.org/wiki/recursive-backtracking/#:~:text=Recursive%20Backtracking,(one%20of%20the%20leaves).
'''

def is_valid_line(arr):
    '''
    Function to check if a row or column is valid
    '''
    visited = set()
    for element in arr:
        if element == 0:
            continue
        elif element in visited:
            return False
        visited.add(element)
    return True

def is_valid_board(board):
    '''
    Function to check if a sudoku board is valid
    '''
    N = len(board)
    for i in range(N):
        row = board[i]
        column = [board[x][i] for x in range(N)]
        if not is_valid_line(row) or not is_valid_line(column):
            return False
    return True

def solve_sudoku(board, N):
    size = len(board)
    if N == 0:
        return is_valid_board(board)
    for i in range(size):
        for j in range(size):
            cell = board[i][j]
            if cell != 0:
                continue
            for num in range(1, size+1):
                board[i][j] = num
                if solve_sudoku(board, N-1) and is_valid_board(board):
                    return True
                board[i][j] = 0
    return False

Board = [ [ 0 , 0 , 0 ],
          [ 1 , 0 , 0 ],
          [ 0 , 3 , 1 ] ]

solve_sudoku(Board, 6)

print(Board)
