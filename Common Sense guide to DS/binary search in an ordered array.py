class Ordered_Array():
    def __init__(self, list):
        self.list = sorted(list)

    def append(self, value):
        if len(self.list)==0:
            self.list.append(value)
        else:
            index = 0
            while(value>=self.list[index]):
                index+=1
                if index >= len(self.list):
                    break
            self.list.insert(index, value)

    def linear_search(self, value):
        index = 0
        while(value>=self.list[index]):
            if value==self.list[index]:
                print("The number of steps taken is {}".format(index))
                return index
            index+=1
            if index >= len(self.list):
                break
        print("The number of steps taken is {}".format(index))
        return False

    def binary_search(self, value):
        first_index = 0
        last_index = len(self.list)-1
        steps = 0
        while(first_index<=last_index):
            middle_index = (first_index + last_index)//2
            if value == self.list[middle_index]:
                steps+=1
                print("The number of steps taken is {}".format(steps))
                return middle_index
            elif value<self.list[middle_index]:
                last_index = middle_index-1
                steps+=1
            else:
                first_index = middle_index + 1
                steps+=1
        print("The number of steps taken is {}".format(steps))
        return False


    def __str__(self):
        return str(self.list)

arr1 = Ordered_Array([])
arr1.append(2)
arr1.append(3)
arr1.append(7)
arr1.append(6)
arr1.append(4)
arr1.append(13)
arr1.append(12)
arr1.append(10)

print(arr1)
print(arr1.binary_search(5))
