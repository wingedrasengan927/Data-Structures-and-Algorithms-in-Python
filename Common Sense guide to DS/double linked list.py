
# A node in a double linked list has linking to it's previous node and next node
# class Node():
#     def __init__(self, value=None, next_node=None, previous_node=None):
#         self.value = value
#         self.previous_node = previous_node
#         self.next_node = next_node

# a double inked list is defined by it's head and tail
class DoublyLinkedList:
    def __int__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    #
    # def insert_at_end(self, value):
    #     '''inserts a value at the end of the array'''
    #
    #     # convert the value into a node object
    #     insert_node = Node(value)
    #     # current element
    #     current = self.head
    #
    #     # if there is no element in the head
    #     if not current:
    #         self.head=insert_node
    #     # inserting when there is a head element
    #     else:
    #         while current:
    #             # inserting at the end
    #             if not current.next_node:
    #                 current.next_node = insert_node
    #                 insert_node.previous_node = current
    #                 self.tail = insert_node
    #             else:
    #                 current = current.next_node
    #
    # def print(self):
    #     '''prints the elements in a doubly linked list'''
    #
    #     #current element
    #     current = self.head
    #     # list to keep the values
    #     alist = []
    #     while current:
    #         alist.append(current.value)
    #         if not current.next_node:
    #             break
    #         else:
    #             current = current.next_node
    #     print(alist)

# creating a doubly linked list
dll = DoublyLinkedList()

# let's add the elements
print(dll.head)
