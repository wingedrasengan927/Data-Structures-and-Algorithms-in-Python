
def bubble_sort(array):
    unsorted_till_index = len(array)-1
    while True:
        swaps = 0
        for i in range(unsorted_till_index):
            # swap if condition
            if array[i]>array[i+1]:
                # swap
                array[i], array[i+1] = array[i+1], array[i]
                swaps+=1
        unsorted_till_index -=1
        # if no swaps, break the loop
        if swaps==0:
            break

arr1 = [4, 2, 7, 1, 3]
bubble_sort(arr1)
print(arr1)

