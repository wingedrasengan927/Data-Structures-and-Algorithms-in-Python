# linked list
# instead of indices like in an array, linked list object has reference to the next element associated with it

# let's create a class for an object in a linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data # the value of this element
        self.next = next # the next element

    # method to get the length of a linked list
    @staticmethod
    def countNodes(head):
        count = 0
        i = head
        while i != None:
            count += 1
            i = i.next
        return count

# instantiating the linked list objects
boxA = Node(4)
boxB = Node(2)
boxC = Node(3)
boxD = Node(10)
boxE = Node(2)

# linking the objects
boxA.next = boxB
boxB.next = boxC
boxC.next = boxD
boxD.next = boxE

print(boxA.data)
print(boxB.data)
print(boxA.next.data)

print(Node.countNodes(boxA))