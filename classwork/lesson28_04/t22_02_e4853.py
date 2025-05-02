from collections import deque

n, m = map(int, input().split())
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * (n + 1)
parent = [-1] * (n + 1)

queue = deque()
queue.append(a)
dist[a] = 0

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            parent[v] = u
            queue.append(v)

if dist[b] == -1:
    print(-1)
else:
    path = []
    current = b
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(dist[b])
    print(*path)
