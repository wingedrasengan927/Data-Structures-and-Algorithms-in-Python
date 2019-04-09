
# binary tree
# each parent can have a maximum 2 children

# tree node class
class TreeNode:
    def __init__(self, value=None, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild =leftChild
        self.rightChild = rightChild

# tree
class BinaryTree:
    def __init__(self, root=None):
        self.root = TreeNode(root)

    def search(self, value):
        '''searches for a given value and returns true if found'''

        return self.searchhelper(value, self.root)

    def searchhelper(self, value, node):
        '''helper for the search function'''

        # if there is a value in the node then only search
        if node:
            # base case
            # if the value is found, return True
            if value == node.value:
                return True
            else:
                # very elegant way of writing the code
                # run the searchhelper function on both the left and right subtrees
                # first the left one runs till the base case is reached, and next the right one
                return self.searchhelper(value, node.leftChild) or self.searchhelper(value, node.rightChild)
        return False

    def print(self):
        '''prints the tree using pre-order depth first search'''

        return self.printhelper(self.root, "")[:-1]

    def printhelper(self, node, traversal):
        '''helper for the print function'''

        if node:
            traversal += (str(node.value) + "-")
            traversal = self.printhelper(node.leftChild, traversal)
            traversal = self.printhelper(node.rightChild, traversal)
        return traversal



# Set up tree
tree = BinaryTree(1)
tree.root.leftChild = TreeNode(2)
tree.root.rightChild = TreeNode(3)
tree.root.leftChild.leftChild = TreeNode(4)
tree.root.leftChild.rightChild = TreeNode(5)

# let's search
print(tree.print())