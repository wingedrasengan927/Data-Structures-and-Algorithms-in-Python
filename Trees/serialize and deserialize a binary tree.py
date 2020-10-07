# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        result = []
        while queue:
            children = []
            for node in queue:
                result.append(node.val if node != None else None)
                if not node:
                    continue
                children.append(node.left)
                children.append(node.right)
            queue = children
        return result
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # make node objects from the data
        nodes = [TreeNode(val) if val != None else None for val in data]
        reversed_nodes = []
        for node in reversed(nodes):
            reversed_nodes.append(node)
        root = reversed_nodes.pop()
        for node in nodes:
            if node == None:
                continue
            node.left = reversed_nodes.pop()
            node.right = reversed_nodes.pop()
        return root