n, s, f = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
from collections import deque
visited = [-1] * n
queue = deque()
queue.append(s - 1)
visited[s - 1] = 0
while queue:
    v = queue.popleft()
    for i in range(n):
        if matrix[v][i] and visited[i] == -1:
            visited[i] = visited[v] + 1
            queue.append(i)
print(visited[f - 1] if visited[f - 1] != -1 else 0)
