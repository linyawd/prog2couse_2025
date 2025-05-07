n, k, a, b, d = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(k):
    u, v = map(int, input().split())
    g[u].append(v)

def dfs(u, depth, visited):
    if depth > d:
        return 0
    if u == b:
        return 1
    count = 0
    for v in g[u]:
        if v not in visited:
            count += dfs(v, depth + 1, visited | {v})
    return count

print(dfs(a, 0, {a}))
