def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y, parent, rank):
    xr = find(x, parent)
    yr = find(y, parent)
    if xr == yr:
        return False
    if rank[xr] < rank[yr]:
        parent[xr] = yr
    else:
        parent[yr] = xr
        if rank[xr] == rank[yr]:
            rank[xr] += 1
    return True

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
used = [False] * m
parent = list(range(n + 1))
rank = [0] * (n + 1)
cost1 = 0
tree = []

for i, (w, u, v) in enumerate(edges):
    if union(u, v, parent, rank):
        cost1 += w
        used[i] = True
        tree.append(i)

cost2 = float('inf')
for banned in tree:
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cnt = 0
    total = 0
    for i, (w, u, v) in enumerate(edges):
        if i == banned:
            continue
        if union(u, v, parent, rank):
            total += w
            cnt += 1
    if cnt == n - 1:
        cost2 = min(cost2, total)

print(cost1, cost2)
