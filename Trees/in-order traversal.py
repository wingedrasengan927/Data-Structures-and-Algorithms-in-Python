def inorder_traversal(root):
    result = []
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        # notice we are appending only valid nodes to the stack
        result.append(node.val)
        node = node.right
    return result