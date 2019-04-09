
# let's create a class for an object in a linked list
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

# This is the linked list class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # method to get the position of value in a list
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        current_position = 1
        while current:
            if current_position == position:
                return current
            current = current.next
            current_position += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        current_position = 1
        if position>1:
            while current and current_position<position:
                if current_position == position-1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                current_position+=1
        elif position ==1:
            new_element.next = self.head
            self.head = new_element


    def delete_value(self, value):
        current = self.head
        if self.head.value == value:
            self.head = self.head.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next= current.next.next
                    break
                else:
                    current=current.next

    def __str__(self):
        current = self.head
        contents = []
        while current:
            contents.append(current.value)
            current = current.next
        return str(contents)



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

print(ll)
# Test delete
ll.delete_value(1)
# Should print 2 now
print(ll)
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)