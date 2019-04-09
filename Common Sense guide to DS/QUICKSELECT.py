def partition(array, leftend, rightend):

    leftpointer = leftend
    rightpointer = rightend-1

    # the pivot is the rightmost element
    pivot_index = rightend
    pivot_value = array[pivot_index]

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
        else:
            temp = array[leftpointer]
            array[leftpointer] = array[rightpointer]
            array[rightpointer] = temp

    temp = array[pivot_index]
    array[pivot_index] = array[leftpointer]
    array[leftpointer] = temp

    return leftpointer

# ----------ALWAYS USE RETURN FOR RECURSIVE FUNCTIONS--------------


# Now let's define the quickselect function
# it is used to find out the kth lowest value in the array without completely sorting the array
# it combines both binary search and quicksort

# let's define a quickselect helper
def quickselecthelper(array, kth_lowest_value, leftend, rightend):

    if leftend<=rightend:
        # let's grab the pivot index first
        pivot_index = partition(array, leftend, rightend)

        if kth_lowest_value<pivot_index:
            return quickselecthelper(array, kth_lowest_value, leftend, pivot_index-1)

        elif kth_lowest_value>pivot_index:
            return quickselecthelper(array, kth_lowest_value, pivot_index+1, rightend)

        else:
            return array[pivot_index]

    else:
        return None

def quickselect(array, kth_lowest_value):
    return quickselecthelper(array, kth_lowest_value, 0, len(array)-1)

arr1 = [54,26,93,17,77,31,44,55,20]
print(quickselect(arr1, 0))