from disjoint_sets_tree import DisjointSet

class Solution(object):
    '''
    The idea is we find union of friends where there is a 1 in the matrix
    and at the end after finding all unions,
    the number of friends circles is the number of sets
    '''
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