"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for."""

def binary_search(input_array, value):
    input_list = sorted(input_array)
    first_index = 0
    last_index = len(input_list) - 1
    print("The original list is: {}".format(input_array))
    print("the sorted list is {}".format(input_list))
    print()
    i=0
    while(first_index<=last_index): # basically means if there is more than one item
        print("This is Iteration {}".format(i+1))
        index=(first_index+last_index)//2
        middle_index = (len(input_list)-1)//2
        middle_element = input_list[middle_index]
        print("The middle element is {}".format(middle_element))
        if first_index==last_index:
            break
        if value==middle_element:
            return index
        elif value>middle_element:
            input_list = input_list[(middle_index+1):]
            print("{} > {}".format(value, middle_element))
            print("New array is {}".format(input_list), "\n")
            first_index=index+1
            i+=1
        elif value<middle_element:
            input_list=input_list[:(middle_index+1)]
            print("{} < {}".format(value, middle_element))
            print("New array is {}".format(input_list), "\n")
            last_index=index
            i+=1
        print()
    return -1

test_list = [1,3,9,11,15,19,29]
test_val2 = 9
print(binary_search(test_list, test_val2))