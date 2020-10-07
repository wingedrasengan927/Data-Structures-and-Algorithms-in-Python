'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

example
---------
sum = 22

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

output: True
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, _sum):
        return self.helper(root, 0, _sum)
        
    def helper(self, node, current_sum, required_sum):
        
        if not node:
            return False
        
        current_sum += node.val
        
        if node.left == None and node.right == None:
            if current_sum == required_sum:
                return True
            else:
                return False
            
        return self.helper(node.left, current_sum, required_sum) or self.helper(node.right, current_sum, required_sum)
            
        
        