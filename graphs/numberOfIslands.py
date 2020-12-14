class Solution:
    def numIslands(self, grid):
        labels = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        cluster_id = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '0' or labels[i][j] != 0:
                    continue
                cluster_id += 1
                labels[i][j] = cluster_id
                self.DFS(i, j, grid, labels, cluster_id)
        return cluster_id
        
        
    def DFS(self, x, y, grid, labels, cluster_id):
        if grid[x][y] == '0':
            return
        neighbours = self.get_neighbours(x, y, grid)
        for i, j in neighbours:
            if labels[i][j] != 0 or grid[i][j] == '0':
                continue
            labels[i][j] = cluster_id
            self.DFS(i, j, grid, labels, cluster_id)
        
    def get_neighbours(self, x, y, grid):
        rows = len(grid)
        columns = len(grid[0])
        neighbours = []
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if i < 0 or j < 0 or i >= rows or j >= columns:
                continue
            neighbours.append([i, j])
        return neighbours