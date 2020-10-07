class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root, val):
    if not root:
        return None
    
    root_val = root.val
    
    if root_val == val:
        return root
    
    elif root_val < val:
        return self.searchBST(root.right, val)
    
    else:
        return self.searchBST(root.left, val)

def searchBSTIteratively(self, root, val):
    
    stack = [root]
    node = root
    
    while stack:
        node = stack.pop()
        if not node:
            continue
        node_val = node.val
        if node_val == val:
            return node
        elif node_val < val:
            stack.append(node.right)
        else:
            stack.append(node.left)
            
    return None

def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    
    if not root:
        return TreeNode(val)
    
    root_val = root.val
    
    if root_val < val:
        if root.right:
            self.insertIntoBST(root.right, val)
        else:
            root.right = TreeNode(val)
            
    else:
        if root.left:
            self.insertIntoBST(root.left, val)
        else:
            root.left = TreeNode(val)
            
    return root

def insertIntoBSTIteratively(self, root, val):
    if not root:
        return TreeNode(val)
    
    stack = [root]
    node = root
    
    while stack:
        node = stack.pop()
        node_val = node.val
        if node_val < val:
            if node.right:
                stack.append(node.right)
            else:
                node.right = TreeNode(val)
        else:
            if node.left:
                stack.append(node.left)
            else:
                node.left = TreeNode(val)
    return root