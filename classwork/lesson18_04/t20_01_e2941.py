import math

class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = 1 << math.ceil(math.log2(k))
        self.tree = 2 * n * [0]
        self.size = n

        for i in range(k):
            self.tree[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def sum(self, l, r):
        l += self.size
        r += self.size

        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
            if r % 2 == 0:
                res += self.tree[r]

            l = (l + 1) // 2
            r = (r - 1) // 2
        return res

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        i = i // 2
        while i > 1:
            self.tree[i] = self.tree[i * 2] + self.tree[2 * i + 1]
            i //= 2

    def print(self):
        print(self.tree)

if __name__ == '__main__':

    with open("input.txt") as file:
        n, t = map(int, file.readline().split())
        arr = list(map(int, file.readline().split()))
        tree = SegmentTree(arr)
        for _ in range(t):
            c, *args = file.readline().split()
            a, b = map(int, args)
            if c == "=":
                tree.update(a - 1, b)
            elif c == "?":
                print(tree.sum(a - 1, b - 1))