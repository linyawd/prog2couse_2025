import sys
import threading
from array import array

def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))
    idx = 0

    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    m = data[idx]
    idx += 1

    size = 1
    while size < n:
        size <<= 1
    tree = array('Q', [0] * (2 * size))  # змінено

    for i in range(n):
        tree[size + i] = a[i]
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    def update(pos, value):
        pos += size
        tree[pos] = value
        while pos > 1:
            pos >>= 1
            tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

    def find_prefix_sum(v):
        if tree[1] <= v:
            return n
        pos = 1
        acc = 0
        while pos < size:
            if tree[2 * pos] + acc <= v:
                acc += tree[2 * pos]
                pos = 2 * pos + 1
            else:
                pos = 2 * pos
        return pos - size

    res = []
    while idx < len(data):
        t = data[idx]
        idx += 1
        if t == 1:
            v = data[idx]
            idx += 1
            res.append(str(find_prefix_sum(v)))
        else:
            x = data[idx] - 1
            y = data[idx + 1]
            idx += 2
            update(x, y)

    print('\n'.join(res))

threading.Thread(target=main).start()
