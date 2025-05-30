from collections import defaultdict

class Node:
    def __init__(self, is_leaf=False, result=None):
        self.children = []
        self.is_leaf = is_leaf
        self.result = result

n = int(input())
nodes = [Node() for _ in range(n + 1)]
parent_map = defaultdict(list)

for i in range(2, n + 1):
    parts = input().split()
    if parts[0] == 'L':
        parent = int(parts[1])
        result = int(parts[2])
        nodes[i] = Node(is_leaf=True, result=result)
        parent_map[parent].append(i)
    else:
        parent = int(parts[1])
        parent_map[parent].append(i)

for parent, children in parent_map.items():
    nodes[parent].children.extend(children)

def dfs(u, first_player_turn):
    if nodes[u].is_leaf:
        return nodes[u].result
    results = [dfs(child, not first_player_turn) for child in nodes[u].children]
    return max(results) if first_player_turn else min(results)

res = dfs(1, True)
print(f'+{res}' if res > 0 else res)
