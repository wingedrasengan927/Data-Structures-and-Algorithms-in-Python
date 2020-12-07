'''
Problem: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/
'''
class DisjointSet(object):
    '''
    The idea is we perform union of a two stones if they are in the same row or same column
    and then return sum(rank-1 for rank in sets)
    Note that here we are concerned about ranks and update accordingly
    '''
    def __init__(self, N):
        self.rank = [1]*N
        self.parent = [i for i in range(N)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)
        
        if parentx == parenty:
            return
        
        if self.rank[parentx] >= self.rank[parenty]:
            self.parent[parenty] = parentx
            self.rank[parentx] += self.rank[parenty]
            self.rank[parenty] = 0
        else:
            self.parent[parentx] = parenty
            self.rank[parenty] += self.rank[parentx]
            self.rank[parentx] = 0
                    
        
class Solution:
    def removeStones(self, stones):
        N = len(stones)
        ds = DisjointSet(N)
        
        for i in range(N):
            for j in range(N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    ds.union(i, j)
        
        maxMoves = 0
        for i in range(N):
            if ds.rank[i] > 1:
                maxMoves += ds.rank[i]-1 # -1 because we cannot remove all stones
            
        return maxMoves
                