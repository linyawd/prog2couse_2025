def find(x, parent):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y, parent, rank):
    xroot = find(x, parent)
    yroot = find(y, parent)
    if xroot == yroot:
        return False
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1
    return True

t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    edges = []
    pq_weight = None
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        if (u == p and v == q) or (u == q and v == p):
            pq_weight = w

    edges.sort()
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    included = False

    for w, u, v in edges:
        if union(u, v, parent, rank):
            if (u == p and v == q) or (u == q and v == p):
                included = True

    print("YES" if included else "NO")
