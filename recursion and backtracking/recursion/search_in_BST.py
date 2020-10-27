# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        
        if root.val == val:
            return root
        
        is_left_subtree = self.searchBST(root.left, val)
        is_right_subtree = self.searchBST(root.right, val)
        
        return is_left_subtree or is_right_subtree