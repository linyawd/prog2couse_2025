n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
visited = [False] * n
stack = [0]
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        for neighbor in g[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
print("YES" if all(visited) else "NO")
