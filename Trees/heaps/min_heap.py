class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.heap = self.build_heap(self.heap)

    def peek(self):
        return self.heap[0]

    def insert(self, val):
        '''
        When we insert a new value, we add it to the bottom of the heap,
        and then siftUp
        '''
        self.heap.append(val)
        self.siftUp(len(self.heap) - 1)

    def remove(self, val):
        '''
        First we find the index of the val to be removed,
        and then swap the element with the bottom most node in the heap,
        and then we sift down the node at the index
        '''
        try:
            to_remove_idx = self.heap.index(val)
            self.swap(to_remove_idx, len(self.heap)-1)
            to_remove_val = self.heap.pop()
            self.siftDown(to_remove_idx)
            return to_remove_val
        except:
            print("Value doesn't exist in the heap")
            return None


    def siftDown(self, parent_node_idx):
        '''
        The idea is to compare the parent node to both of it's children
        and we swap the parent with the smallest child whose value is 
        less than the parent.
        The time complexity in both siftUp and siftDown is O(logN)
        '''
        # get children
        child_one_idx = 2*parent_node_idx + 1
        child_two_idx = 2*parent_node_idx + 2

        heap_size = len(self.heap)
        if child_one_idx < heap_size and child_two_idx < heap_size:
            child_one_val = self.heap[child_one_idx]
            child_two_val = self.heap[child_two_idx]

            if child_one_val <= child_two_val:
                child_to_swap_idx = child_one_idx
            else:
                child_to_swap_idx = child_two_idx

            if self.heap[parent_node_idx] > self.heap[child_to_swap_idx]:
                self.swap(parent_node_idx, child_to_swap_idx)
        else:
            if child_one_idx < heap_size:
                child_to_swap_idx = child_one_idx
            elif child_two_idx < heap_size:
                child_to_swap_idx = child_two_idx
            else:
                return

            if self.heap[parent_node_idx] > self.heap[child_to_swap_idx]:
                self.swap(parent_node_idx, child_to_swap_idx)
        
        self.siftDown(child_to_swap_idx)

    def siftUp(self, child_node_idx):
        '''
        The idea is to compare the child node to it's parent node
        and swap it if the parent node value is greater than child node
        and repeat the process
        '''
        # edge case
        if child_node_idx == 0 or child_node_idx >= len(self.heap):
            return

        # find parent node idx
        parent_node_idx = (child_node_idx-1) // 2

        child_node_val = self.heap[child_node_idx]
        parent_node_val = self.heap[parent_node_idx]

        if child_node_val < parent_node_val:
            self.swap(child_node_idx, parent_node_idx)

        self.siftUp(parent_node_idx)

    def swap(self, idx_1, idx_2):
        self.heap[idx_1], self.heap[idx_2] = self.heap[idx_2], self.heap[idx_1]

    def build_heap(self, array):
        '''
        1. We always represent heap as an array, not as a separate data structure
        2. to build a heap from an array, we call sift down on all the parent nodes starting from the bottom
        3. This has O(N) time complexity,
        4. but if we run sift up , it's going to take O(NlogN) time
        '''
        bottom_first_parent_idx = (len(array) - 2) // 2
        for i in reversed(range(bottom_first_parent_idx + 1)): # + 1 because we are dealing with index here
            self.siftDown(i)
        return array

    def __repr__(self):
        return str(self.heap)

array = [102, 23, 12, 18, 17, 30, 44, 9, 31]
heap = MinHeap(array)
print(heap)