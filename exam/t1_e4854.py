n = int(input())
g = [[] for _ in range(n)]
for i in range(n):
    line = input().strip()
    if line:
        g[i] = list(map(int, line.split()))

gt = [[] for _ in range(n)]
for u in range(n):
    for v in g[u]:
        gt[v - 1].append(u + 1)

print(n)
for lst in gt:
    lst.sort()
    print(' '.join(map(str, lst)))
