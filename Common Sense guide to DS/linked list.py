

class Node():
    def __init__(self, value=None, next_node=None):
        # the value it will store
        self.value = value
        # the link which points it to the next node
        self.next = next_node

class Linked_List():
    def __init__(self, head = None):
        # A LinkedList is defined by it's head.
        self.head = head

    def append(self, value):
        '''append an element at the end of the array'''
        # current node
        current = self.head
        # reach the end of the array
        while current.next:
            current = current.next
        current.next = Node(value=value)

    def print(self):
        '''prints the elements of the array'''

        # current element
        current = self.head
        alist = []
        while current:
            alist.append(current.value)
            current = current.next
        print(alist)


    def read(self, index):
        '''read the element at a particular index. returns -1 if none'''

        # Let's define the current node
        current = self.head
        # Let's also define the current index and keep track of the index we're in
        current_index =0
        while current:
            # if the index of current node is same as the index we're searching, return it's value
            if current_index == index:
                return current.value
            # else, go to the next node
            else:
                current = current.next
                current_index += 1
        return -1

    def search(self, value):
        '''searches for a particular value in the array'''

        # current element
        current = self.head
        # cuurent index
        current_index = 0
        # iterate through the array till you find the value
        while current:
            if current.value == value:
                return current_index
            current = current.next
            current_index+=1
        # return -1 if the value doesn't exist
        return -1

    def insert(self, value, index):
        '''inserts a node at a given index
        so say if insert at 5, then the new node is between the previous 4th and 5th elements'''

        # let's convert the value into a node object
        insert_node = Node(value)
        # current element
        current = self.head
        # current index
        current_index = 0
        # insertion at any position other than zero
        if index>0:
            while current and current_index<index:
                if current_index == index-1:
                    insert_node.next = current.next
                    current.next = insert_node
                    break
                else:
                    current = current.next
                    current_index+=1
        # insertion at zero
        if index == 0:
            insert_node.next = current
            self.head = insert_node


    def delete(self, index):
        '''delete a node at a particular index'''
        # current element
        current = self.head
        # current index
        current_index = 0
        # deletion at any position other than zero
        if index > 0:
            while current and current_index < index:
                # deleting the last element
                if not current.next.next:
                    current.next = None
                    break
                # deleting the middle elements
                if current_index == index - 1:
                    current.next = current.next.next
                    break
                else:
                    current = current.next
                    current_index += 1
        # deletion at zero
        if index == 0:
            self.head = current.next


# let's create a linked list

# first let's initialize them with their values
a = Node(3)
b = Node(6)
c = Node(1)
d = Node(4)
e = Node(5)

# let's connect the lists
a.next = b
b.next = c
c.next = d
d.next = e

# Let's put them in a linked list
ll = Linked_List(a)
print(ll.read(4))

# let's use the append method
ll.append(6)
ll.append(90)
ll.append(24)
ll.print()
ll.insert(67, 0)
ll.print()
ll.delete(8)
ll.print()