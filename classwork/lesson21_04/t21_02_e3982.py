n = int(input())
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in data[1:]:
        matrix[i][j-1] = 1
for row in matrix:
    print(' '.join(map(str, row)))
