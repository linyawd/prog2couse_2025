import heapq

n, m = map(int, input().split())
s, f = map(int, input().split())
s -= 1
f -= 1

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))

INF = 10**18
dist = [INF] * n
prev = [-1] * n
dist[s] = 0
pq = [(0, s)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in g[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            prev[v] = u
            heapq.heappush(pq, (dist[v], v))

if dist[f] == INF:
    print(-1)
else:
    print(dist[f])
    path = []
    cur = f
    while cur != -1:
        path.append(cur + 1)
        cur = prev[cur]
    print(*path[::-1])
