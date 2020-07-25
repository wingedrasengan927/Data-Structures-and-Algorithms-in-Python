'''
Iterative Solution for Preorder Traversal
'''

def preorder_traversal(root):
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        if not node:
            continue
        result.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return result