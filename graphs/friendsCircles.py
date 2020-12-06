from disjoint_sets_tree import DisjointSet

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet()
        
        n = len(M)

        # make set for each vertex
        for i in range(n):
            ds.make_set(i)

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    ds.union(i, j)
                    
        return ds.num_sets