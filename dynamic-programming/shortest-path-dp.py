class Graph:
    def __init__(self, vertices, edges):
        '''
        Assumption: All the values of nodes are different and unique
        '''
        self.vertices = vertices
        self.edges = edges

    def itervertices(self):
        return self.vertices

    def weight(self, u, v):
        return self.edges[(u, v)]

    def inverse_vertices(self, v):
        return [x for x, y in self.edges.keys() if y == v]

# initializing graph: figure graph
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = {(1, 2): 2, (1, 3): 3, (2, 4): 3, (2, 3): 4, (2, 5): 4, 
            (3, 5): 2, (3, 6): 6, (5, 6): 2,
            (5, 8): 6, (6, 8): 4, (6, 9): 3, (4, 7): 4, (8, 7): 3, (8, 10): 2,
            (9, 10): 4}

graph = Graph(vertices, edges)

class ShortestPathResult:
    def __init__(self):
        self.parent = {}
        self.distance = {}

def shortest_path(graph, s):
    '''
    Find Shortest path from s to all the vertices in the graph using dynamic programming
    Args:
        graph: 2D List
            Weighted DAG
        s: 1D List
            vertex
    '''
    result =  ShortestPathResult()
    result.distance[s] = 0 # base case
    result.parent[s] = None
    for v in graph.itervertices():
        shortest_path_dp(graph, v, result)
    return result

def shortest_path_dp(graph, v, result):
    '''
    Find the Shortest Path to vertex v recursively using dynamic programming
    Args:
        graph: 2D List
            A Weighted DAG
        v: 1D list
            vertex to find the distance
        result:
            result object used for memoization of distance and parent
    '''
    if v in result.distance: # memoization
        return result.distance[v]
    result.distance[v] = float('inf')
    result.parent[v] = None
    for u in graph.inverse_vertices(v):
        current_distance = shortest_path_dp(graph, u, result) + graph.weight(u, v)
        if current_distance < result.distance[v]:
            result.distance[v] = current_distance
            result.parent[v] = u
    return result.distance[v]

result =shortest_path(graph, 1)
print(result.distance)
print(result.parent)
    