# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return
        
        maxDepth = self.getMaxDepth(root)
        
        final_result = []
        for level in range(1, maxDepth+1):
            result = []
            self.helper(root, 1, level, result)
            final_result.append(result)
        
        return final_result
        
    def getMaxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getMaxDepth(root.left), self.getMaxDepth(root.right))
        
        
    def helper(self, node, current_depth, required_depth, result):
        if not node:
            return
        
        if current_depth == required_depth:
            result.append(node.val)
            return
        
        self.helper(node.left, current_depth + 1, required_depth, result)
        self.helper(node.right, current_depth + 1, required_depth, result)