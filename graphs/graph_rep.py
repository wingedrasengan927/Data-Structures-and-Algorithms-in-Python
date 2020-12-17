class Graph:
    '''
    Representation of a graph using adjaceny matrix and adjaceny list.
    This assumes vertices are numbered from 0-N
    '''
    def __init__(self, N):
        self.n_nodes = N
        self.adj_matrix = [[0 for i in range(N)] for j in range(N)]
        self.adj_list = {key: [] for key in range(N)}
    
    def connect(self, u, v, w):
        '''
        u - source
        v - destination
        w - weight
        '''
        self.adj_matrix[u][v] = w

    def make_neighbours(self, u, v):
        self.adj_list[u].append(v)