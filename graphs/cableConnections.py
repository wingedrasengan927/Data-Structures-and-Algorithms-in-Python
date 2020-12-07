'''
Problem: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
'''

class DisjointSet(object):
    def __init__(self, N):
        self.rank = [1]*N
        self.parent = [i for i in range(N)]
        self.num_sets = N
        self.existing_unions = 0
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)
        
        if parentx == parenty:
            self.existing_unions += 1
            return True
        
        if self.rank[parentx] > self.rank[parenty]:
            self.parent[parenty] = parentx
        elif self.rank[parentx] < self.rank[parenty]:
            self.parent[parentx] = parenty
        else:
            self.parent[parenty] = parentx
            self.rank[parentx] += 1
            
        self.num_sets -= 1
        return False

class Solution:
    def makeConnected(self, n, connections):
        '''
        The idea is to count the number of sets after performing all union operatons
        and also count reductant (already existing unions)
        and if n_reductant >= n_sets - 1
         (-1 because we are dealing here with not connected 
         sets and hence we are removing the connected set)
         we return n_sets-1 else -1
        '''
        ds = DisjointSet(n)
        for x, y in connections:
            ds.union(x, y)
        if ds.existing_unions >= ds.num_sets - 1:
            return ds.num_sets - 1
        return -1