class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        n_buckets = 1000
        self.buckets = [None] * n_buckets
        
    
    def get_hash(self, key):
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value = self.get_hash(key)
        if not self.buckets[hash_value]:
            self.buckets[hash_value] = []
                        
        # we iterate through the bucket to find if the key is already present
        # and return the index if it's present else None
        flag = False
        for i in range(len(self.buckets[hash_value])):
            if self.buckets[hash_value][i][0] == key:
                flag = True
                self.buckets[hash_value][i][1] = value
                break
        
        if not flag:
            self.buckets[hash_value].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = self.get_hash(key)
        if not self.buckets[hash_value]:
            return -1
        
            
        for i in range(len(self.buckets[hash_value])):
            if self.buckets[hash_value][i][0] == key:
                return self.buckets[hash_value][i][1]
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value = self.get_hash(key)
        if self.buckets[hash_value]:
            for i in range(len(self.buckets[hash_value])):
                if self.buckets[hash_value][i][0] == key:
                    self.buckets[hash_value].pop(i)
                    break        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)