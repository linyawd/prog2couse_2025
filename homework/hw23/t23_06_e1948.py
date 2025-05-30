from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    indegree[v - 1] += 1

q = deque(i for i in range(n) if indegree[i] == 0)
res = []

while q:
    u = q.popleft()
    res.append(u + 1)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

if len(res) == n:
    print(*res)
else:
    print(-1)
