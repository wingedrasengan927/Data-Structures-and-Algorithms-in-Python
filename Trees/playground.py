# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        depth = self.get_depth(root)
        result = []
        for d in range(1, depth + 1):
            level = []
            result.append(self.levelOrderHelper(root, d, level))

        return result
            
    def levelOrderHelper(self, root, depth, level = []):
        if not root:
            return level
                
        if depth == 1:
            level.append(root.val)
        elif (depth > 1):
            self.levelOrderHelper(root.left, depth-1, level)
            self.levelOrderHelper(root.right, depth-1, level)
                        
        return level
        
        
    def get_depth(self, node):
        if not node:
            return 0
        
        return 1 + max(self.get_depth(node.left), self.get_depth(node.right))