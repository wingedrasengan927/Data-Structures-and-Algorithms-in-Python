# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # The idea is to create a dummy node and assign two pointers to it
        # one pointer would be static and would help in node tracking
        # the other would be used to populate the next pointer
        # the dynamic pointer attaches itself to only existent nodes
        prev = dummy = Node()
        node = root
        while node:
            prev.next = node.left
            if prev.next:
                prev = prev.next
            prev.next = node.right
            if prev.next:
                prev = prev.next
            node = node.next
            if not node:
                prev = dummy
                node = prev.next
        return root

    def connectLevelOrderv2(self, root):
        # works for any binary tree
        if not root:
            return None
        
        queue = [root]
        while queue:
            level = []
            children = []
            for node in queue:
                if not node:
                    continue
                level.append(node)
                children.append(node.left)
                children.append(node.right)
                
            for i in range(len(level)-1):
                j = i + 1
                node1 = level[i]
                node2 = level[j]
                node1.next = node2
                
            queue = children
        
        return root

    def connectLevelOrderv1(self, root):
        # Only works in case of a perfect binary tree
        if not root:
            return None
        
        queue = [root]
        while queue:
            children = []
            for i in range(len(queue)):                
                node1 = queue[i]
                if not node1:
                    continue
                
                j = i + 1
                if j == len(queue):
                    children.append(node1.left)
                    children.append(node1.right)
                    break
                    
                node2 = queue[j]
                    
                node1.next = node2
                children.append(node1.left)
                children.append(node1.right)
                
            queue = children
        return root

    def connectRecursively(self, root):
        # Only works in case of a perfect binary tree
        if not root:
            return None
        
        if root.left:
            root.left.next = root.right
            
        if root.right:
            if root.next:
                root.right.next = root.next.left
                
        self.connect(root.left)
        self.connect(root.right)
        
        return root