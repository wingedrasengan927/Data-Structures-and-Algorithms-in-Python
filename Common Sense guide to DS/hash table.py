

# my version

class HashTable():
    def __init__(self):
        self.table = [None]*10000

    def HashFunction(self, string):
        string = string.upper()
        code = {chr(i): i - 64 for i in range(65, (65 + 26))}
        hashValue = sum([code[i] for i in string])
        return hashValue

    def store(self, string):
        hv = self.HashFunction(string)
        if self.table[hv]:
            self.table[hv].append(string)
        else:
            self.table[hv] = [string]

    def lookup(self, string):
        hv = self.HashFunction(string)
        if self.table[hv]:
            if string in self.table[hv]:
                return True
        return False

    def __repr__(self):
        return str(self.table)

x = HashTable()
x.store("ABC")
x.store("CAB")
print(x.lookup("ABC"))

