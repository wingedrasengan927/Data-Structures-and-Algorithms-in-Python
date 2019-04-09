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
                return index
            index+=1
            if index >= len(self.list):
                break
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
print(arr1.linear_search(8))