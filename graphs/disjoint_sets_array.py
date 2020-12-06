class DisjointSet(object):
    def __init__(self, n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx == parenty:
            return

        if self.rank[parentx] > self.rank[parenty]:
            self.parent[parenty] = parentx
        elif self.rank[parentx] < self.rank[parenty]:
            self.parent[parentx] = parenty
        else:
            self.parent[parenty] = parentx
            self.rank[parentx] += 1