'''
Problem: https://leetcode.com/problems/rotting-oranges/submissions/
'''

class Solution:
    def orangesRotting(self, grid):
        '''
        The trick is to use levels and children while doing BFS
        as done in BFS in trees
        '''
        rows = len(grid)
        columns = len(grid[0])
        queue = []
        visited = set()
        total_oranges = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] > 0:
                    total_oranges += 1
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append([i, j])
        minute = 0
        while len(queue) > 0:
            children = []
            for level in queue:
                x, y = level
                neighbours = self.get_neighbours(x, y, grid)
                for i, j in neighbours:
                    if grid[i][j] == 0 or (i, j) in visited:
                        continue
                    children.append([i, j])
                    visited.add((i, j))
            queue = children
            if len(queue) > 0:
                minute += 1   
        unvisited_oranges = total_oranges - len(visited)
        if unvisited_oranges > 0:
            return -1
        return minute
        
    def get_neighbours(self, x, y, grid):
        rows = len(grid)
        columns = len(grid[0])
        neighbours = []
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if i < 0 or j < 0 or i>=rows or j>=columns:
                continue
            neighbours.append([i, j])
        return neighbours