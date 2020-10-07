def levelorder_traversal(root):
    result = []
    queue = [root]
    while queue:
        level = []
        children = []
        for node in queue:
            if not node:
                continue
            level.append(node.val)
            children.append(node.left)
            children.append(node.right)
        if len(level) > 0:
            result.append(level)
        queue = children
    return result