from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        '''
        Using BFS to find shortest distance between start and end vertex
        '''
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        queue = deque()
        result = [[0 for i in range(N)] for j in range(N)]
        queue.append((0, 0))
        result[0][0] = 1
        while len(queue) > 0:
            x, y = queue.popleft()
            neighbours = self.get_neighbours(x, y, grid)
            for i, j in neighbours:
                if grid[i][j] == 1 or result[i][j]!=0:
                    continue
                result[i][j] = result[x][y] + 1
                queue.append((i, j))
        if result[N-1][N-1] == 0:
            return -1
        return result[N-1][N-1]
                
    def get_neighbours(self, x, y, grid):
        N = len(grid)
        neighbours = []
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1], [x+1, y+1], [x+1, y-1], [x-1, y+1], [x-1, y-1]]:
            if i < 0 or j < 0 or i>=N or j>=N:
                continue
            neighbours.append([i, j])
        return neighbours