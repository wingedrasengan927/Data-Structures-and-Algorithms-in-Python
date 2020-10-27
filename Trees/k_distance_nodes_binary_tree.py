'''
Find all nodes which are at a distance k from a given node in a binary tree
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        '''
        The idea is simple:
        1. Do BFS while level <= K
        2. To do BFS, we require the parent node of each node
        3. So we build a dictionary that has a mapping of node to its parent
        4. We Perfom BFS and return result
        '''
        if not root:
            return []
        if K == 0:
            return [target.val]
        # get parent mapping dict
        parent_mapping = self.get_parent_mapping(root)
        # perfom BFS
        queue = [target]
        visited = set()
        visited.add(target)
        result = []
        level = 1
        while queue and level <= K:
            next_level = []
            for node in queue:
                neighbours = [node.left, node.right, parent_mapping.get(node)]
                for neighbour in neighbours:
                    if not neighbour:
                        continue
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    next_level.append(neighbour)
                    if level == K:
                        result.append(neighbour.val)
            queue = next_level
            level += 1
            
        return result
        
        
    def get_parent_mapping(self, root):
        parent_mapping = dict()
        self.get_parent_mapping_helper(root, parent_mapping)
        return parent_mapping
    
    def get_parent_mapping_helper(self, root, mapping_dict):
        if root.left:
            mapping_dict[root.left] = root
            self.get_parent_mapping_helper(root.left, mapping_dict)
            
        if root.right:
            mapping_dict[root.right] = root
            self.get_parent_mapping_helper(root.right, mapping_dict)