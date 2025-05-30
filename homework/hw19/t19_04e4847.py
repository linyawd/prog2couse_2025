import sys

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.position = {}

    def push(self, id, priority):
        self.heap.append([priority, id])
        self.position[id] = len(self.heap) - 1
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._sift_down(0)
        del self.position[top[1]]
        print(f"{top[1]} {top[0]}")

    def change(self, id, new_priority):
        i = self.position[id]
        old_priority = self.heap[i][0]
        self.heap[i][0] = new_priority
        if new_priority > old_priority:
            self._sift_up(i)
        else:
            self._sift_down(i)

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] > self.heap[p][0]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < n and self.heap[l][0] > self.heap[largest][0]:
                largest = l
            if r < n and self.heap[r][0] > self.heap[largest][0]:
                largest = r
            if largest != i:
                self._swap(i, largest)
                i = largest
            else:
                break

    def _swap(self, i, j):
        self.position[self.heap[i][1]], self.position[self.heap[j][1]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

pq = PriorityQueue()
for line in sys.stdin:
    parts = line.strip().split()
    if parts[0] == 'ADD':
        pq.push(parts[1], int(parts[2]))
    elif parts[0] == 'POP':
        pq.pop()
    elif parts[0] == 'CHANGE':
        pq.change(parts[1], int(parts[2]))
