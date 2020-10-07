# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

'''
example
    1
   / \\
  2   2
 / \ / \\
3  4 4  3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        return self.recursiveMirror(root, root)
        
    def recursiveMirror(self, nodeA, nodeB):

        # base case
        if nodeA == None and nodeB == None:
            return True
        elif nodeA == None or nodeB == None:
            return False

        return self.recursiveMirror(nodeA.left, nodeB.right) and self.recursiveMirror(nodeA.right, nodeB.left) and nodeA.val == nodeB.val