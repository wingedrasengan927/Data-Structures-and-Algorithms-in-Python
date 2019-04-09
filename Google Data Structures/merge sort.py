def mergeSort(alist):
    # splitting
    print("Splitting the list: ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        print("The left half is: ", lefthalf)
        print("the right half is: ", righthalf)
        print()

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        # merging the list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging the list: ",alist)

alist = [21, 4, 1, 3, 9, 20, 25]
mergeSort(alist)
print(alist)
