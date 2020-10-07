# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        
        if not root:
            return True
        
        stack = []
        current_node = root
        previous_val = float('-inf')
        
        while stack or current_node:
            
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
                
            current_node = stack.pop()
            
            current_val = current_node.val
            
            if current_val <= previous_val:
                return False
            
            previous_val = current_val
            current_node = current_node.right
            
        return True
    
    def isValidBSTRecursive(self, root):
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            val = root.val

            if val <= lower or val >= upper:
                return False

            if not helper(root.right, val, upper):
                return False
            if not helper(root.left, lower, val):
                return False
            return True

        return helper(root)