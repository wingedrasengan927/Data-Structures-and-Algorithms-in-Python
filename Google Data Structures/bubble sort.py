
# bubble sort
# naive approach

def bubble_sort(input_array):
    print("The original array is {}".format(input_array), "\n")
    for i in range(len(input_array)-2):
        print("This is iteration {}".format(i+1))
        for j in range(len(input_array)-1):
            if input_array[j]>input_array[j+1]:
                temp = input_array[j+1]
                input_array[j+1] = input_array[j]
                input_array[j]=temp
        print("The new array is {}".format(input_array))
    return input_array

arr1 = [12, 23, 343, 21, 67,55 , 3, 67]

print(bubble_sort(arr1))