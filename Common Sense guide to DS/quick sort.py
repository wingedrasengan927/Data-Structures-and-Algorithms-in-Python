
# ------------READ THE NEW ONE ---------------

# Let's define our partition function first
# generally, the last element is kept is kept as the pivot
# We'll also pass in the left pointer and right pointer also as an argument
# Like this, we'll be able to partition a part of an array defined by it's pointers
# Which we'll be used in quicksort

def partition(array, left_pointer, right_pointer):
    # right pointer is just before the pivot
    pivot_index = right_pointer+1
    while(left_pointer<=right_pointer):
        count = 0
        # count is to check whether the pointers are moving or not
        if array[left_pointer]<array[pivot_index]:
            left_pointer += 1
            count+=1
        if array[right_pointer] >array[pivot_index]:
            right_pointer -= 1
            count+=1
        if count == 0:
            # if count is 0, the pointers are not moving. So, SWAP
            temp = array[left_pointer]
            array[left_pointer] = array[right_pointer]
            array[right_pointer] = temp
    # finally, swap the left pointer and the pivot
    temp = array[pivot_index]
    array[pivot_index] = array[left_pointer]
    array[left_pointer] = temp
    return left_pointer

# Let's implement the quicksort algorithm
def quicksort(array, left_pointer, right_pointer):
    print("Current array: {}".format(array))
    print("Current left pointer: {}".format(left_pointer))
    print("Current right pointer: {}".format(right_pointer))
    print()
    # base case
    if right_pointer<left_pointer:
        return
    # define the pivot
    pivot_index = partition(array, left_pointer, right_pointer)
    # quicksort the lest array
    quicksort(array, left_pointer, pivot_index-2)
    # quicksort the right array
    quicksort(array, pivot_index+1, right_pointer)



arr1 = [0, 5, 2, 1, 6, 3]
quicksort(arr1, 0, 4)
print(arr1)


import random

random.seed(101)

arr1 = [random.randrange(100) for i in range(10)]
print(arr1)
quicksort(arr1, 0, len(arr1)-2)
print(arr1)