class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            
        return current_node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            
        else:        
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        
        return

            
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
        
        else:
            current_node = self.head
            for i in range(self.length - 1):
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
        
        self.length += 1
        
        return
            

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        
        if index == 0:
            return self.addAtHead(val)
        
        if index == self.length:
            return self.addAtTail(val)
        
        new_node = Node(val)
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            
        previous_node = current_node.prev
        current_node.prev = new_node
        new_node.next = current_node
        new_node.prev = previous_node
        previous_node.next = new_node
        
        self.length += 1
        
        return
        


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index >= self.length:
            return
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            
        previous_node = current_node.prev
        next_node = current_node.next
        
        if previous_node:
            previous_node.next = next_node
        else:
            self.head = next_node
            
        if next_node:
            next_node.prev = previous_node
        
        self.length -= 1
        
        return
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)