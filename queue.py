__author__ = "Paarth Bhasin"
__title__ = "Assignment-3 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '20/8/2016'
__studentID__ = 26356104
__LastModified__ = '24/10/2016'


class Queue:
    def __init__(self, size):
        assert size > 0, "size should be positive"
        self.the_array = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_full(self):
        return self.rear >= len(self.the_array)

    def is_empty(self):
        return self.count == 0

    def reset(self):
        self.front = 0
        self.rear = 0
        self.count = 0

    def append(self, new_item):
        assert not self.is_full(), "Queue is full"
        self.the_array[self.rear] = new_item
        self.rear = (self.rear + 1) % len(self.the_array)
        self.count += 1

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.the_array[self.front]
        self.front = (self.front + 1) % len(self.the_array)
        self.count -= 1
        return item

    def print(self):
        index = self.front
        for _ in range(self.count):
            print(str(self.the_array[index]))
            index = (index + 1) % len(self.the_array)
