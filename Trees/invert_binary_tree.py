# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        return root

    def invertTreeIteratively(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            # swap
            temp = node.left
            node.left = node.right
            node.right = temp
            
            stack.append(node.right)
            stack.append(node.left)
        return root