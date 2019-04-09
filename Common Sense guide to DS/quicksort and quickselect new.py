

# let's define our partition function

# this function takes in three arguments
# 1. the array 2. the leftmost element of the array 3. the rightmost element
# the pivot is going to be the right most element
def partition(array, leftend, rightend):

    # let's define the pointers
    # the left pointer is the starting element
    # the right pointer is the one before pivot
    leftpointer = leftend
    rightpointer = rightend-1

    # the pivot is the rightmost element
    pivot_index = rightend
    pivot_value = array[pivot_index]

    # let's use this as a flag to know when we are done
    done = False

    while not done:

        # move the leftpointer to the right until we obtain a value greater than the pivot and do not cross the right pointer
        while array[leftpointer] <= pivot_value  and leftpointer<=rightpointer:
            leftpointer += 1

        # move the right pointer to the left until we obtain a value less than the pivot and do not cross the left pointer
        while array[rightpointer] >= pivot_value  and rightpointer>=leftpointer:
            rightpointer -= 1

        # once the leftpointer is greater than rightpointer the process is done
        if leftpointer>rightpointer:
            done = True
        # if not, let's swap the pointer values and repeat the process again
        else:
            temp = array[leftpointer]
            array[leftpointer] = array[rightpointer]
            array[rightpointer] = temp

    # once the entire process is done and leftpointer crosses rightpointer,
    # swap the pivot value with the leftpointer
    # and return the leftpointer which is the new pivot index
    temp = array[pivot_index]
    array[pivot_index] = array[leftpointer]
    array[leftpointer] = temp

    return leftpointer

# this is a helper for the quicksort function
# don't define pointers in this function
# since they're already present in the partition function
def quicksorthelper(array, leftend, rightend):

    # it runs only when the leftend is less than the right end
    # base case
    if leftend < rightend:

        # Let's grab the pivot index
        pivot_index = partition(array, leftend, rightend)

        # let's divide the array into left array and right array by the pivot
        # and recursively run the function on each of them

        quicksorthelper(array, leftend, pivot_index-1)
        quicksorthelper(array, pivot_index+1, rightend)
        return array


# this is the actual quicksort function
def quicksort(array):
    return quicksorthelper(array, 0, len(array)-1)

# Now let's define the quickselect function
# it is used to find out the kth lowest value in the array without completely sorting the array
# it combines both binary search and quicksort

# let's define a quickselect helper
def quickselecthelper(array, kth_lowest_value, leftend, rightend):

    if leftend<=rightend:

        # let's grab the pivot index first
        pivot_index = partition(array, leftend, rightend)

        # if the required index is less than the pivot index, we recursively run the function on the left array
        if kth_lowest_value<pivot_index:
            return quickselecthelper(array, kth_lowest_value, leftend, pivot_index-1)

        # if the required index is greater than the pivot index, we recursively run the function on the right array
        elif kth_lowest_value>pivot_index:
            return quickselecthelper(array, kth_lowest_value, pivot_index+1, rightend)

        # if the required index is equal to the pivot index, we return that value
        else:
            return array[pivot_index]

    else:
        return None


# this is the quickselect function
def quickselect(array, kth_lowest_value):
    return quickselecthelper(array, kth_lowest_value, 0, len(array)-1)



arr1 = [54,26,93,17,77,31,44,55,20]
print(quicksort(arr1))
