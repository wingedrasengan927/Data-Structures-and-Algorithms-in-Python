class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        n_buckets = 1000
        self.buckets = [None] * n_buckets
        
    def hashFunction(self, val):
        return val % len(self.buckets)
        
    def add(self, key: int) -> None:
        # a hashset should have only unique elements
        hashVal = self.hashFunction(key)
        if self.buckets[hashVal]:
            if key not in self.buckets[hashVal]:
                self.buckets[hashVal].append(key)
        else:
            self.buckets[hashVal] = [key]

    def remove(self, key: int) -> None:
        hashVal = self.hashFunction(key)
        if self.buckets[hashVal]:
            if key in self.buckets[hashVal]:
                self.buckets[hashVal].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashVal = self.hashFunction(key)
        if self.buckets[hashVal]:
            if key in self.buckets[hashVal]:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)