

# restraints of a binary search tree
# 1. each node has either zero, one, or two children
# 2. If a node has two children, it must have one child that has a lesser value than the parent,
# and one child that has a greater value than the parent.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        '''searches for a given value with efficiency O(logN) and returns the particular node'''

        return self.searchhelper(value, self.root)

    def searchhelper(self, value, node):
        '''helper for the search function'''

        # if node has some value in it
        if node:
            # if value found, return the node
            if value == node.value:
                return node
            # if value is less than the node and leftChild has some value in it, run the function on leftChild recursively
            elif value<node.value and node.leftChild:
                return self.searchhelper(value, node.leftChild)
            # if value is greater than the node and rightChild has some value in it, run the function on rightChild recursively
            elif value>node.value and node.rightChild:
                return self.searchhelper(value, node.rightChild)
        # if node has no value and we reached the end of the tree, return None
        return None

    def insert(self, value):
        '''inserts a value at the end of a tree'''

        return self.inserthelper(value, self.root)

    def inserthelper(self, value, node):
        '''helper for the insert function'''

        # first we'll check if there is a root for our tree
        # if not, we'll put the node as the root
        if self.root is None:
            self.root  = TreeNode(value)

        # if node has a value
        elif node is not None:
            # if value is less than the node,
            # run the function on the left sub-tree if the leftChild has value
            # if leftChild is empty, append the new value to it
            if value<=node.value:
                if node.leftChild:
                    return self.inserthelper(value, node.leftChild)
                else:
                    # base case
                    node.leftChild = TreeNode(value)
            # if value is greater than the node,
            # run the function on the right sub-tree if the rightChild has value
            # if rightChild is empty, append the new value to it
            elif value>node.value:
                if node.rightChild:
                    return self.inserthelper(value, node.rightChild)
                else:
                    # base case
                    node.rightChild = TreeNode(value)

    def print(self):
        '''prints the tree in a pre-order depth first search traversal'''

        return self.printhelper(self.root, "")[:-1]

    def printhelper(self, node, traversal):
        '''helper for the print function'''

        if node:
            traversal += str(node.value) + "-"
            traversal = self.printhelper(node.leftChild, traversal)
            traversal = self.printhelper(node.rightChild, traversal)
        return traversal

    def delete(self, value):
        '''deletes a particular node'''

        return self.deletehelper(value, self.root)

    def deletehelper(self, value, node):
        '''helper for the delete function'''

        # to delete a node, we have to assign None to the entire node
        # the best way to do this is to return a None value
        # remember, to delete a node, don't put it's value attribute to None

        # first, we have to search for the value to be deleted

        # base case
        # if we've traversed beneath the bottom of the tree, return None
        if node is None:
            return None

        # If the value we're deleting is less or greater than the current node,
        # we set the left or right child respectively to be
        # the return value of a recursive call of this very method on the current node's left or right subtree.

        elif value < node.value:
            node.leftChild = self.deletehelper(value, node.leftChild)
            return node
        elif value > node.value:
            node.rightChild =  self.deletehelper(value, node.rightChild)
            return node

        # so this is what happens. say, we search for 11
        # and let us assume we did not put value == node.value condition

        # running function(11, 50):
        #   11<50
        #   node.leftChild = function(11, 25)
        #   running function(11, 25):
        #       11<25
        #       node.leftChild = function(11, 10)
        #       running function(11, 10)
        #           11>10
        #           node.rightChild = function(11, 11)
        #           running function(11, 11) --> returns nothing. So, base case reached
        #           node.rightChild = None (since the function(11, 11) returns nothing) ; Now, run the next line
        #           return 10
        #       function(11, 10) = 10
        #       node.leftChild = function(11, 10) = 10
        #       return 25
        #   function(11, 25) = 25
        #   node.leftChild = function(11, 25) = 25
        #   return 50

        # hence, 11 has been deleted
        # this can be used to delete values at height 0 only

        # If the current node is the one we want to delete:
        elif node.value == value:

            # node being deleted has no children, delete it
            if (node.leftChild or node.rightChild) is None:
                return None

            # If the current node has no left child, we delete it by
            # returning its right child (and it's subtree if existent)
            # Now, the current node is replaced by it's right child
            elif node.rightChild and not node.leftChild:
                return node.rightChild
            elif node.leftChild and not node.rightChild:
                return node.leftChild

            # If the current node has two children, we delete the current node
            # by calling the successor function (below), which changes the current node's
            # value to the value of its successor node:
            else:
                node.rightChild = self.successor(node.rightChild, node)
                return node


    def successor(self, node, node_to_delete):
        '''finds the successor node of a particular node'''

        # If the current node of this function has a left child,
        # we recursively call this function to continue down
        # the left subtree to find the successor node.
        if node.leftChild:
            node.leftChild = self.successor(node.leftChild, node_to_delete)
            return node
        # If the current node has no left child, that means the current node
        # of this function is the successor node, and we take its value
        # and make it the new value of the node that we're deleting:
        else:
            node_to_delete.value = node.value
            # We return the successor node's right child
            # Now, the successor node is replaced by it's right child
            # if there is no rightChild to successor node, it is replaced by None
            return node.rightChild

    def postorder_print(self):
        '''prints in tree in a post order depth first manner'''

        return self.postorder_print_helper(self.root, "")[:-1]

    def postorder_print_helper(self, node, traversal):
        '''helper for the post order print function'''

        if node:
            traversal = self.postorder_print_helper(node.leftChild, traversal)
            traversal += str(node.value) + "-"
            traversal = self.postorder_print_helper(node.rightChild, traversal)
        return traversal


# setting up the tree

arr1 = [50, 25, 75, 10, 33, 4, 11, 30, 40, 56, 89, 52, 61, 82, 95]
tree = BinarySearchTree()
for i in arr1:
    tree.insert(i)

print(tree.print())

# let's test the delete function
tree.delete(50)

print(tree.postorder_print())


