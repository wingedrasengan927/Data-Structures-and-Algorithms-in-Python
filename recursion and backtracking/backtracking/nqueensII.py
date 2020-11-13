'''
Given a chess board of size nxn.
find out the number of distinct ways you can place n queens

Solution
---------
The way it is different from nqueens I is that
1) There we have found a solution if we exhausted all the N pieces
2) Here, we cannot recurse over N because then we would be aiming for the wrong solution
   Which is: distict ways you can place n queens + n-1 queens + n-2 queens ...
3) So instead here we would have achieved our goal if we exhaused all the chessboard space
   i.e we would be recursing over the number of rows
4) Since our goal is to find all the possible solutions, we backtrack even if we find a solution
'''

class Solution:
    def totalNQueens(self, n):
        board = [[0 for x in range(n)] for y in range(n)]
        return self.totalNQueensHelper(0, n, board)
    
    def totalNQueensHelper(self, row, N, board):
        if row == N:
            # we have exhausted the search space
            # meaning, we have found a solution
            return 1
        
        solutions = 0
        
        for col in range(N):
            if self.is_attacked(row, col, board):
                continue
                
            board[row][col] = 1
            solutions += self.totalNQueensHelper(row+1, N, board)
            board[row][col] = 0
            
        return solutions
        
        
    def is_attacked(self, x, y, board):
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