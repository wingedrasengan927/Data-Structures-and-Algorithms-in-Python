# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # The idea is to take root from postorder traversal by popping up the stack,
        # since the root will always be at the end.
        # we take the root we got from postorder traversal and find it's position in
        # inorder traversal.
        # In inorder traveral, the elements left to the root make up the left subtree and those
        # to the right make up the right subtree.
        # Hence we recursively repeat the process.
        # But how do we do it recursively?
        # The idea is to keep track of the indices that represent the subtree in the inorder list
        # for example, left idx represents the left most node in the subtree in the inorder list
        # right idx represents the right most node in the subtree in the inorder list
        # this will the basis of our recursion and our base case would be:
        # if left_idx > right_idx: return None 
        # basically we use inorder list to keep track of recursion
        # note that we build the right subtree first because in postorder traversal, the order is
        # left - right - root
        
        inorder_dict = dict()
        for idx, val in enumerate(inorder):
            inorder_dict.update({val: idx})
                    
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            root = TreeNode(postorder.pop())
            root_inorder_idx = inorder_dict[root.val]
            
            root.right = helper(root_inorder_idx + 1, right_idx)
            root.left = helper(left_idx, root_inorder_idx-1)
            
            return root
        
        return helper(0, len(inorder)-1)