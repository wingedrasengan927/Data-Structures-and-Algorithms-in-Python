class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.back = Node()

    def isEmpty(self):
        return self.front == self.back

    def EnQueue(self, val):
        emptyNode = Node()
        self.back.data = val
        self.back.next = emptyNode
        if self.front.data == None:
            self.front = self.back
        self.back = emptyNode

    def DeQueue(self):
        if self.isEmpty():
            return False
        frontVal = self.front.data
        self.front = self.front.next 
        return frontVal

    def traverse(self, startNode, endNode):
        while startNode != None:
            print(startNode.data)
            if startNode == endNode:
                return "Traverse Completed"
            startNode = startNode.next
        return "Traverse Completed"

    def __str__(self):
        return self.traverse(self.front, self.back)

queue = Queue()
queue.EnQueue(12)
queue.EnQueue(15)
queue.EnQueue(34)
queue.DeQueue()
print(queue)