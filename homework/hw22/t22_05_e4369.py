from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

k = int(input())
starts = list(map(int, input().split()))

dist = [-1] * (n + 1)
q = deque()
for s in starts:
    dist[s] = 0
    q.append(s)

while q:
    u = q.popleft()
    for v in g[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

max_dist = max(dist[1:])
ans = [i for i in range(1, n + 1) if dist[i] == max_dist]
print(max_dist)
print(min(ans))
