class Heap:
    def __init__(self):
        self.items = []

    def insert(self, key):
        self.items.append(key)
        i = len(self.items) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.items[i] > self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
                i = parent
            else:
                break

    def extract(self):
        if len(self.items) == 1:
            return self.items.pop()

        root = self.items[0]
        self.items[0] = self.items.pop()
        self._sift_down(0)
        return root

    def _sift_down(self, i):
        size = len(self.items)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < size and self.items[left] > self.items[largest]:
                largest = left
            if right < size and self.items[right] > self.items[largest]:
                largest = right

            if largest == i:
                break

            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            i = largest

if __name__ == '__main__':
    heap = Heap()
    data = list(map(int, input().split()))
    for x in data:
        heap.insert(x)

    sorted_list = []
    while heap.items:
        sorted_list.append(heap.extract())

    print(*sorted_list[::-1])