class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        '''
        The idea is to do DFS from the border only if the data point is 'O' and capture the 
        visited nodes from there.
        *Always keep visited set while doing DFS algorithm.
        '''

        if len(board) == 0:
            return
        visited = set()
        rows = len(board)
        columns = len(board[0])  
        for i in range(rows):
            for j in range(columns):
                if i == 0 or j == 0 or i == rows-1 or j==columns-1:
                    if board[i][j] == 'O':
                        if (i, j) in visited:
                            continue
                        visited.add((i, j))
                        self.DFS(i, j, board, visited)
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O':
                    if (i, j) in visited:
                        continue
                    board[i][j] = 'X'
        
    def DFS(self, i, j, board, visited):
        
        if board[i][j] == 'X':
            return
        neighbours = self.get_neighbours(i, j, board)
        for x, y in neighbours:
            if (x, y) in visited:
                continue
            visited.add((x, y))
            self.DFS(x, y, board, visited)
            
    def get_neighbours(self, i, j, board):
        rows = len(board)
        columns = len(board[0])
        neighbours = []
        for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if x < 0 or y < 0 or x >= rows or y >= columns:
                continue
            neighbours.append([x, y])
        return neighbours