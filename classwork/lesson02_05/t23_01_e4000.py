n, s = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
stack = [s - 1]
count = 0
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        count += 1
        for i in range(n):
            if matrix[node][i] and not visited[i]:
                stack.append(i)
print(count)
