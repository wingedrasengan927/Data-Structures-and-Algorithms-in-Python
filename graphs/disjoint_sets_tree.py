'''
Disjoint Set Implementation using Tree Representation and Collapse find
'''
class Node(object):
    def __init__(self, data, parent=None, rank=0):
        self.data = data
        self.parent = parent
        self.rank = rank
        
class DisjointSet(object):
    def __init__(self):
        self.map = dict()
        self.num_sets = 0
        
    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.map[data] = node
        self.num_sets += 1
        
    def find_set_util(self, node):
        parent = node.parent
        if parent == node:
            return parent
        
        node.parent = self.find_set_util(node.parent) # path compression or collapse find
        return node.parent
    
    def find_set(self, data):
        node = self.map[data]
        return self.find_set_util(node)
    
    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]
        
        # get representative elements
        parent1 = self.find_set_util(node1)
        parent2 = self.find_set_util(node2)
        
        if parent1 == parent2:
            return
        
        if parent1.rank == parent2.rank:
            parent2.parent = parent1
            parent1.rank += 1
        elif parent1.rank > parent2.rank:
            parent2.parent = parent1
        else:
            parent1.parent = parent2
            
        self.num_sets -= 1