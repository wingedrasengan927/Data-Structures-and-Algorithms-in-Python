
def selection_sort(array):
    for i in range(len(array)):
        lowest_so_far = i
        print("The new array is {}".format(arr1))
        print("lowest_so_far is {}".format(array[lowest_so_far]))
        for j in range(i+1, len(array)):
            if array[j]<array[lowest_so_far]:
                lowest_so_far = j
        print("the new lowest_so_far is {}".format(array[lowest_so_far]))
        if lowest_so_far!=i:
            print("swap {} and {}".format(array[lowest_so_far], array[i]))
            temp = array[i]
            array[i] = array[lowest_so_far]
            array[lowest_so_far] = temp
        else:
            print("do nothing")
        print("\n")
    return array

arr1 = [4, 2, 7, 1, 3]
selection_sort(arr1)
print(arr1)
