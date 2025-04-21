n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j]:
            print(i + 1, j + 1)
