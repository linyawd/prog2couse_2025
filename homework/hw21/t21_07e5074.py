n, m = map(int, input().split())
deg = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    deg[u - 1] += 1
    deg[v - 1] += 1

for d in deg:
    print(d)
