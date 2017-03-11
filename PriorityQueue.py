__author__ = 'Paarth Bhasin'


class PriorityQueue:
    def __init__(self):
        self.count = 0
        self.array = [None]

    def __len__(self):
        return self.count

    def reset(self):
        self.array = [None]

    def rise(self, k):
        while k > 1 and self.array[k].duration < self.array[k // 2].duration:
            self.swap(k, k // 2)
            k //= 2

    def add(self, item):
        # print(str(self.count) + " : count")
        # print(str(len(self.array)) + " : length")
        if self.count + 1 < len(self.array):
            self.array[self.count + 1] = item
        else:
            self.array.append(item)

        self.count += 1
        self.rise(self.count)

    def swap(self, k, parent):
        temp = self.array[k]
        self.array[k] = self.array[parent]
        self.array[parent] = temp

    def serve(self):
        minimum = self.array[1]
        self.array[1] = self.array[self.count]
        self.sink(1)
        self.count -= 1
        return minimum

    def sink(self, k):
        while 2 * k <= self.count:
            child = self.smallest_child(k)
            if self.array[k].duration <= self.array[child].duration:
                break
            self.swap(child, k)
            k = child

    def smallest_child(self, k):
        if 2 * k == self.count or self.array[2 * k].duration < self.array[2 * k + 1].duration:
            return 2 * k
        else:
            return 2 * k + 1

    def print(self):
        for i in range(1, self.count):
            print(self.array[i])
