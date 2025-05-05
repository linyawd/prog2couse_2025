n = int(input())
grid = [list(input()) for _ in range(n)]
x, y = map(int, input().split())
x -= 1
y -= 1
visited = [[False] * n for _ in range(n)]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if grid[i][j] == '*' or visited[i][j]:
        return 0
    visited[i][j] = True
    return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

print(dfs(x, y))
