class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)
        i = len(self.data) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.data[i] <= self.data[p]:
                break
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p

    def extract(self):
        res = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        i = 0
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            max_i = i
            if l < len(self.data) and self.data[l] > self.data[max_i]:
                max_i = l
            if r < len(self.data) and self.data[r] > self.data[max_i]:
                max_i = r
            if max_i == i:
                break
            self.data[i], self.data[max_i] = self.data[max_i], self.data[i]
            i = max_i
        return res

heap = MaxHeap()
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == '0':
        heap.insert(int(cmd[1]))
    else:
        print(heap.extract())
