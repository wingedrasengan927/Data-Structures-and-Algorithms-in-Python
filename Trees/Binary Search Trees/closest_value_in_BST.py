'''
Given a target value, return the closet value in BST
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValueBST(root, target):
    # Time Complexity = O(logN)
    # Worst Case Time Complexity = O(N) this occurs if there is a single branch
    # Space Complexity will be the same as time complexity if done recursively else O(1)
    return closestValueBSTHelper(root, target, float('inf'))

def closestValueBSTHelper(root, target, closestVal):
    if not root:
        return closestVal
    if abs(target - root.val) < abs(target - closestVal):
        closestVal = root.val
    if target > root.val:
        return closestValueBSTHelper(root.right, target, closestVal)
    elif target < root.val:
        return closestValueBSTHelper(root.left, target, closestVal)
    else:
        return closestVal

def closestValueBSTIteratively(root, target):
    if not root:
        return None
    closestValue = float('inf')
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            return closestValue
        if abs(target - node.val) < abs(target - closestValue):
            closestValue = node.val
        if target > node.val:
            stack.append(node.right)
        elif target < node.val:
            stack.append(node.left)
        else:
            break
    return closestValue