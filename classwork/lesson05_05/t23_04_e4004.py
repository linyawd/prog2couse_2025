n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

def dfs(u):
    visited[u] = 1
    for v in range(n):
        if graph[u][v]:
            if visited[v] == 1:
                return True
            if visited[v] == 0 and dfs(v):
                return True
    visited[u] = 2
    return False

for i in range(n):
    if visited[i] == 0 and dfs(i):
        print(1)
        break
else:
    print(0)
