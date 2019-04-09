
# in an ordered array, everything is sorted
# It sorts as soon as we append

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

    def __str__(self):
        return str(self.list)

arr1 = Ordered_Array([])
arr1.append(2)
arr1.append(3)
arr1.append(7)
arr1.append(6)
arr1.append(4)

print(arr1)

