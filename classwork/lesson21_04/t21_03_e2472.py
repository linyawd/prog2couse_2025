n = int(input())
k = int(input())
adj = [[] for _ in range(n + 1)]
res = []
for _ in range(k):
    op = input().split()
    if op[0] == '1':
        u = int(op[1])
        v = int(op[2])
        adj[u].append(v)
        adj[v].append(u)
    else:
        u = int(op[1])
        print(' '.join(map(str, adj[u])))

