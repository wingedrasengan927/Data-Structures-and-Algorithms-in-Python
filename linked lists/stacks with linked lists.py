class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = self.bottom = Node()

    def isEmpty(self):
        return self.top == self.bottom

    def pop(self):
        if self.isEmpty():
            return False
        topElement = self.top.data
        self.top = self.top.next
        return topElement

    def push(self, val):
        emptyNode = Node(val)
        emptyNode.next = self.top
        self.top = emptyNode

    def traverse(self, startNode, endNode):
        while startNode != None:
            print(startNode.data)
            if startNode == endNode:
                break
            startNode = startNode.next
        return "Traversal complete"

    def __str__(self):
        return self.traverse(self.top, self.bottom)

stack = Stack()
stack.push(12)
stack.push(7)
stack.pop()
print(stack)

