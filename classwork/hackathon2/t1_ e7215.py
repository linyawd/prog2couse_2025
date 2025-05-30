from collections import deque

m, n = map(int, input().split())
grid = [list(input()) for _ in range(m)]
start = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == '+':
            start = (i, j)

dirs = [(-1, 0, 'n'), (1, 0, 's'), (0, -1, 'w'), (0, 1, 'e')]
queue = deque()
queue.append((start[0], start[1], ""))
visited = [[False]*n for _ in range(m)]
visited[start[0]][start[1]] = True

def is_exit(x, y):
    return (x == 0 or x == m-1 or y == 0 or y == n-1) and grid[x][y] in (' ', '+')

if is_exit(start[0], start[1]):
    print(0)
    print()
else:
    found = False
    while queue:
        x, y, path = queue.popleft()
        for dx, dy, move in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == ' ':
                if is_exit(nx, ny):
                    print(len(path)+1)
                    print(path + move)
                    found = True
                    break
                visited[nx][ny] = True
                queue.append((nx, ny, path + move))
        if found:
            break
    if not found:
        print(-1)
