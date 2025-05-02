n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    degree = 0
    for j in range(n):
        degree += matrix[i][j]
    print(degree, end=' ')
