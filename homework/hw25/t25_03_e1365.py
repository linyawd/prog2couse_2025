n, s, f = map(int, input().split())
s -= 1
f -= 1
graph = [list(map(int, input().split())) for _ in range(n)]

INF = 10**18
dist = [INF] * n
dist[s] = 0

for _ in range(n - 1):
    for u in range(n):
        for v in range(n):
            if graph[u][v] != -1 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

print(-1 if dist[f] == INF else dist[f])
