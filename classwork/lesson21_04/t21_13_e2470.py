n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
valid = True
for i in range(n):
    if matrix[i][i] != 0:
        valid = False
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            valid = False
print("YES" if valid else "NO")
