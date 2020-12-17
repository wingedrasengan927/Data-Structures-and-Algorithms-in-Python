'''
problem: https://leetcode.com/problems/01-matrix/submissions/
'''

from collections import deque

class Solution:
    def updateMatrix(self, matrix):
        '''
        This is a multi source BFS problem
        explanation: https://leetcode.com/problems/01-matrix/discuss/101080/Python-Simple-with-Explanation
        (down in the comments)
        '''
        queue = deque()
        rows = len(matrix)
        columns = len(matrix[0])
        result = [[-1 for j in range(columns)] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    result[i][j] = 0
                    
        while len(queue) > 0:
            x, y = queue.popleft()
            for i, j in self.get_neighbours(x, y, matrix):
                if result[i][j] == -1:
                    result[i][j] = result[x][y] + 1
                    queue.append((i, j))
        return result
    
    def get_neighbours(self, x, y, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        neighbours = []
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if  i<0 or j<0 or i>=rows or j>=columns:
                continue
            neighbours.append([i, j])
        return neighbours