from disjoint_sets_tree import DisjointSet

class Solution(object):
    def NumberOfIslands(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet()
        
        n = len(M)
        m = len(M[0])

        # make set for each vertex
        for i in range(n):
            for j in range(m):
                # print(i, j, i*m+j)
                if M[i][j] == 1:
                    ds.make_set(i*m + j)

        for i in range(n):
            for j in range(m):
                if M[i][j] == 0:
                    continue
                if i+1 < n and M[i+1][j] == 1:
                    ds.union(i*m + j, (i+1)*m + j)
                if i-1 >= 0 and M[i-1][j] == 1:
                    ds.union(i*m + j, (i-1)*m + j)
                if j+1 < m and M[i][j+1] == 1:
                    ds.union(i*m + j, i*m + j+1)
                if j-1 >=0 and M[i][j-1] == 1:
                    ds.union(i*m + j, i*m + j-1)

        return ds.num_sets