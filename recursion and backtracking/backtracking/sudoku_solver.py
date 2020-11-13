'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
'''

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """        
        _set = set()
        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val != ".":
                    _set.add((row, val))
                    _set.add((val, col))
                    _set.add((row//3, col//3, val))       
                    
        self.sudokuHelper(board, _set)
        
    def sudokuHelper(self, board, _set):
        row, col = self.find_empty_cell(board)
        if row == -1 and col == -1:
            return True

        for val in range(1, len(board)+1):
            val = str(val)
            if not self.is_valid(row, col, val, _set):
                continue
            _set.add((row, val))
            _set.add((val, col))
            _set.add((row//3, col//3, val))
            board[row][col] = val
            if self.sudokuHelper(board, _set):
                return True
            board[row][col] = "."
            _set.remove((row, val))
            _set.remove((val, col))
            _set.remove((row//3, col//3, val))
        return False
        
    def find_empty_cell(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    return row, col
        return -1, -1
            
        
    def is_valid(self, row, col, val, _set):
        if (row, val) in _set or (val, col) in _set or (row//3, col//3, val) in _set:
            return False
        return True