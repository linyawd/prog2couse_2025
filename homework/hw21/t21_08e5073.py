n, m = map(int, input().split())
edges = set()

has_multiedge = False
for _ in range(m):
    u, v = map(int, input().split())
    if (u, v) in edges:
        has_multiedge = True
        break
    edges.add((u, v))

print("YES" if has_multiedge else "NO")
