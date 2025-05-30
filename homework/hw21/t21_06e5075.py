n, m = map(int, input().split())
in_deg = [0] * n
out_deg = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    out_deg[u - 1] += 1
    in_deg[v - 1] += 1

for i in range(n):
    print(in_deg[i], out_deg[i])
