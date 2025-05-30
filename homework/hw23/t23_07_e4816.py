import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

visited = [False] * n
components = []

def dfs(u, comp):
    visited[u] = True
    comp.append(u + 1)
    for v in adj[u]:
        if not visited[v]:
            dfs(v, comp)

for i in range(n):
    if not visited[i]:
        comp = []
        dfs(i, comp)
        components.append(comp)

print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)
