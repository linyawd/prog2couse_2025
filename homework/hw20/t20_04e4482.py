import sys
import threading
import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

class SegmentTree:
    def __init__(self, data, func):
        self.n = len(data)
        self.func = func
        self.data = data
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.data[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2*v+1, tl, tm)
            self.build(2*v+2, tm+1, tr)
            self.tree[v] = self.func(self.tree[2*v+1], self.tree[2*v+2])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0 if self.func == math.gcd else 1
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left = self.query(2*v+1, tl, tm, l, min(r, tm))
        right = self.query(2*v+2, tm+1, tr, max(l, tm+1), r)
        return self.func(left, right)

    def update(self, v, tl, tr, pos, val):
        if tl == tr:
            self.tree[v] = val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2*v+1, tl, tm, pos, val)
            else:
                self.update(2*v+2, tm+1, tr, pos, val)
            self.tree[v] = self.func(self.tree[2*v+1], self.tree[2*v+2])

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx+n]))
    idx += n
    m = int(data[idx])
    idx += 1

    gcd_tree = SegmentTree(a, math.gcd)
    lcm_tree = SegmentTree(a, lcm)

    res = []
    for _ in range(m):
        q = int(data[idx])
        l = int(data[idx+1]) - 1
        r = int(data[idx+2]) - 1
        idx += 3
        if q == 1:
            g = gcd_tree.query(0, 0, n-1, l, r)
            c = lcm_tree.query(0, 0, n-1, l, r)
            if g < c:
                res.append("wins")
            elif g > c:
                res.append("loser")
            else:
                res.append("draw")
        else:
            gcd_tree.update(0, 0, n-1, l, r+1)
            lcm_tree.update(0, 0, n-1, l, r+1)

    print('\n'.join(res))

threading.Thread(target=main).start()
