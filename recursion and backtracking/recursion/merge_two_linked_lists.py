class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            current_node = l1
            l1 = l1.next
        else:
            current_node = l2
            l2 = l2.next
            
        current_node.next = self.mergeTwoLists(l1, l2)
            
        return current_node