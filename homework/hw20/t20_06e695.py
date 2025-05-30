import sys
import threading

def main():
    input = sys.stdin.read
    data = input().split()

    def formula(n):
        return (n * n % 12345) + (n * n * n % 23456)

    N = 100001
    a = [formula(i) for i in range(1, N + 1)]
    size = 1
    while size < N:
        size *= 2

    max_tree = [0] * (2 * size)
    min_tree = [0] * (2 * size)

    for i in range(N):
        max_tree[size + i] = min_tree[size + i] = a[i]

    for i in range(size - 1, 0, -1):
        max_tree[i] = max(max_tree[2*i], max_tree[2*i + 1])
        min_tree[i] = min(min_tree[2*i], min_tree[2*i + 1])

    def range_query(l, r):
        l += size
        r += size + 1
        max_val = -float('inf')
        min_val = float('inf')
        while l < r:
            if l % 2 == 1:
                max_val = max(max_val, max_tree[l])
                min_val = min(min_val, min_tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                max_val = max(max_val, max_tree[r])
                min_val = min(min_val, min_tree[r])
            l //= 2
            r //= 2
        return max_val - min_val

    def point_update(pos, value):
        pos += size
        max_tree[pos] = min_tree[pos] = value
        pos //= 2
        while pos:
            max_tree[pos] = max(max_tree[2*pos], max_tree[2*pos + 1])
            min_tree[pos] = min(min_tree[2*pos], min_tree[2*pos + 1])
            pos //= 2

    k = int(data[0])
    idx = 1
    res = []
    for _ in range(k):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        if x > 0:
            l = x - 1
            r = y - 1
            res.append(str(range_query(l, r)))
        else:
            pos = -x - 1
            point_update(pos, y)

    print('\n'.join(res))

threading.Thread(target=main).start()
