# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        return self.reverseListHelper(None, head)
        
    def reverseListHelper(self, previous_node, current_node):
        if not current_node:
            return previous_node
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        
        return self.reverseListHelper(previous_node, current_node)