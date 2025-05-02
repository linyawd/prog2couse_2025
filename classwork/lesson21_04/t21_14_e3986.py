n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
sources = []
sinks = []
for i in range(n):
    in_deg = out_deg = 0
    for j in range(n):
        out_deg += matrix[i][j]
        in_deg += matrix[j][i]
    if in_deg == 0:
        sources.append(i + 1)
    if out_deg == 0:
        sinks.append(i + 1)
print(len(sources), *sources)
print(len(sinks), *sinks)
