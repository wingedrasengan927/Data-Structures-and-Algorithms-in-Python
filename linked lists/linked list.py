class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize head with a dummy node
        self.head = Node()

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        currentNode = self.head
        for i in range(index):
            if currentNode.data == None:
                return -1
            currentNode = currentNode.next
            
        if currentNode.data == None:
            return -1
        return currentNode.data
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        currentNode = self.head
        while currentNode.data != None:
            previousNode = currentNode
            currentNode = currentNode.next
        newNode = Node(val)
        previousNode.next = newNode
        newNode.next = currentNode
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
            
        currentNode = self.head
        for i in range(index):
            if currentNode.data == None:
                return -1
            previousNode = currentNode
            currentNode = currentNode.next
            
        newNode = Node(val)
        previousNode.next = newNode
        newNode.next = currentNode
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return
        
        currentNode = self.head
        for i in range(index):
            if currentNode.data == None:
                return -1
            previousNode = currentNode
            currentNode = currentNode.next
            
        if currentNode.data == None:
            return -1
        
        previousNode.next = currentNode.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)