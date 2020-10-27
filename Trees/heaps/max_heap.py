class MaxHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def siftDown(self, parent_node_idx, array):
        array_size = len(array)
        child_node_one_idx = 2*parent_node_idx + 1
        child_node_two_idx = 2*parent_node_idx + 2
        while child_node_one_idx < array_size:
            if child_node_two_idx < array_size:
                child_node_one_val = array[child_node_one_idx]
                child_node_two_val = array[child_node_two_idx]
                if child_node_one_val >= child_node_two_val:
                    child_to_swap_idx = child_node_one_idx
                else:
                    child_to_swap_idx = child_node_two_idx
                
                if array[child_to_swap_idx] > array[parent_node_idx]:
                    self.swap(child_to_swap_idx, parent_node_idx, array)
                    parent_node_idx = child_to_swap_idx
                    child_node_one_idx = 2*parent_node_idx + 1
                    child_node_two_idx = 2*parent_node_idx + 2 
                else:
                    break
            else:
                if array[child_node_one_idx] > array[parent_node_idx]:
                    self.swap(child_node_one_idx, parent_node_idx, array)
                    break

    def siftUp(self, child_node_idx, array):
        parent_node_idx = (child_node_idx - 1) // 2
        while child_node_idx > 0 and array[parent_node_idx] < array[child_node_idx]:
            self.swap(child_node_idx, parent_node_idx, array)
            child_node_idx = parent_node_idx
            parent_node_idx = (child_node_idx - 1) // 2

    def build_heap(self, array):
        bottom_first_parent_node_idx = (len(array) - 2) // 2
        for i in reversed(range(bottom_first_parent_node_idx + 1)):
            self.siftDown(i, array)
        return array
        
    def insert(self, val):
        self.heap.append(val)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self, val):
        try:
            idx_to_remove = self.heap.index(val)
            last_idx = len(self.heap) - 1
            self.swap(idx_to_remove, last_idx, self.heap)
            removed_val = self.heap.pop()
            self.siftDown(idx_to_remove, self.heap)
            return removed_val
        except:
            print("Value not found")
            return None
    
    def __repr__(self):
        return str(self.heap)

    def swap(self, idx_i, idx_j, array):
        array[idx_i], array[idx_j] = array[idx_j], array[idx_i]


array = [102, 23, 12, 18, 17, 30, 44, 9, 31]
heap = MaxHeap(array)
print(heap)