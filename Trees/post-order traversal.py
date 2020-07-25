def postorder_traversal(root):
    result = []
    stack = [(False, root)]
    while stack:
        is_visited, node = stack.pop()
        if not node:
            continue
        if is_visited:
            result.append(node.val)
        else:
            stack.append((True, node))
            stack.append((False, node.right))
            stack.append((False, node.left))
    return result