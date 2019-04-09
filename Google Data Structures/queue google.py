
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    # add an element at the end of the queue
    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

    def __str__(self):
        return str(self.storage)

q = Queue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())
print(q)
print(q.peek())