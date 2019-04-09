
# A node in a double linked list has linking to it's previous node and next node
class Node:
    def __init__(self, value=None, next_node=None, previous_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

# a double inked list is defined by it's head and tail
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def insert_at_end(self, value):
        '''inserts a value at the end of the array with efficiency O(1)'''

        # convert the value into a node object
        insert_node = Node(value)

        # if there is no element in the head, make the new node head
        # the tail will also be the same element since there is only one element
        if not self.head:
            self.head=insert_node
            self.tail = insert_node

        # inserting when there is a head element
        else:
            # the previous node attribute of the new node must point towards the current tail
            insert_node.previous_node = self.tail
            # the next node attribute of the current tail must point towards the new node\
            self.tail.next_node = insert_node
            # the new node should be declared as the new current tail
            self.tail = insert_node

    def remove_from_front(self):
        '''removes the head with efficiency O(1)'''

        # if there is no head, return -1
        if not self.head:
            return -1
        # if there is head
        elif self.head:
            # the new head is the next node of the current head
            self.head = self.head.next_node

    def print(self):
        '''prints the elements in a doubly linked list'''

        #current element
        current = self.head
        # list to keep the values
        alist = []
        while current:
            alist.append(current.value)
            if not current.next_node:
                break
            else:
                current = current.next_node
        print(alist)


"Since doubly linked lists can insert data at the end in O(1) time and delete data from the front in O(1) time,"
"they make the perfect underlying data structure for a queue."


# let's make a Queue class based off the doubly linked list

class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enque(self, value):
        '''inserts a value at the end'''

        self.queue.insert_at_end(value)

    def deque(self):
        '''removes a value from the front'''

        self.queue.remove_from_front()

    def print(self):
        '''prints all the elements in the queue'''

        self.queue.print()


# creating a doubly linked list
dll = DoublyLinkedList()

# let's add the elements
dll.insert_at_end(4)
dll.insert_at_end(3)
dll.insert_at_end(1)
dll.insert_at_end(7)
dll.insert_at_end(6)
dll.insert_at_end(9)

# let's remove elements
dll.remove_from_front()
dll.remove_from_front()
dll.remove_from_front()
dll.remove_from_front()
dll.remove_from_front()
dll.remove_from_front()
dll.remove_from_front()

# let's print the elements
dll.print()

# it works

print()

# let's test our Queue class

q = Queue()
q.enque(3)
q.deque()
q.print()

# it works
