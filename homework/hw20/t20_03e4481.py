import sys
import threading
import math


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    m = int(data[n + 1])
    queries = data[n + 2:]

    size = 4 * n
    tree = [0] * size

    def build(v, tl, tr):
        if tl == tr:
            tree[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            build(2 * v + 1, tl, tm)
            build(2 * v + 2, tm + 1, tr)
            tree[v] = math.gcd(tree[2 * v + 1], tree[2 * v + 2])

    def query(v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return tree[v]
        tm = (tl + tr) // 2
        left = query(2 * v + 1, tl, tm, l, min(r, tm))
        right = query(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        return math.gcd(left, right)

    def update(v, tl, tr, pos, val):
        if tl == tr:
            tree[v] = val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                update(2 * v + 1, tl, tm, pos, val)
            else:
                update(2 * v + 2, tm + 1, tr, pos, val)
            tree[v] = math.gcd(tree[2 * v + 1], tree[2 * v + 2])

    build(0, 0, n - 1)

    i = 0
    out = []
    for _ in range(m):
        q = int(queries[i])
        l = int(queries[i + 1]) - 1
        r = int(queries[i + 2])
        if q == 1:
            out.append(str(query(0, 0, n - 1, l, r - 1)))
        else:
            update(0, 0, n - 1, l, r)
        i += 3

    print('\n'.join(out))


threading.Thread(target=main).start()
