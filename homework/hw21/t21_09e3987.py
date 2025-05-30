n, m = map(int, input().split())
edges = set()

for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    edges.add((u, v))

expected = n * (n - 1) // 2
print("YES" if len(edges) == expected else "NO")
