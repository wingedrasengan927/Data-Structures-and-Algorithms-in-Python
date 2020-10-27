class HeapSort:
    def siftDown(self, parent_node_idx, end_idx, array):

        child_node_one_idx = 2*parent_node_idx + 1
        child_node_two_idx = 2*parent_node_idx + 2
        while child_node_one_idx <= end_idx:
            if child_node_two_idx <= end_idx:
                child_node_one_val = array[child_node_one_idx]
                child_node_two_val = array[child_node_two_idx]
                if child_node_one_val >= child_node_two_val:
                    child_to_swap_idx = child_node_one_idx
                else:
                    child_to_swap_idx = child_node_two_idx
                
                if array[child_to_swap_idx] > array[parent_node_idx]:
                    self.swap(parent_node_idx, child_to_swap_idx, array)
                    parent_node_idx = child_to_swap_idx
                    child_node_one_idx = 2*parent_node_idx + 1
                    child_node_two_idx = 2*parent_node_idx + 2
                else:
                    break
            else:
                if array[child_node_one_idx] >  array[parent_node_idx]:
                    self.swap(parent_node_idx, child_node_one_idx, array)
                    break

    def swap(self, idx_one, idx_two, array):
        array[idx_one], array[idx_two] = array[idx_two], array[idx_one]

    def build_heap(self, array):
        bottom_first_parent_idx = (len(array) - 2) // 2
        end_idx = len(array) - 1
        for i in reversed(range(bottom_first_parent_idx + 1)):
            self.siftDown(i, end_idx, array)
        return array

    def sort(self, array):
        # time - O(N(logN))
        # space - O(1)

        # build heap
        array = self.build_heap(array) # O(N)

        end_idx = len(array) - 1
        root_idx = 0
        while end_idx > 0: # O(NlogN)
            self.swap(root_idx, end_idx, array)
            end_idx -= 1
            self.siftDown(root_idx, end_idx, array)

        return array

array = [8,5,2,9,5,6,3]
heap_sort = HeapSort()
print(heap_sort.sort(array))