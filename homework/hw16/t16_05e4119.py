from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)

def insert(root, path_parts):
    if not path_parts:
        return
    insert(root.children[path_parts[0]], path_parts[1:])

def print_tree(node, depth=0):
    for key in sorted(node.children):
        print(' ' * depth + key)
        print_tree(node.children[key], depth + 1)

n = int(input())
root = Node()
for _ in range(n):
    path = input()
    insert(root, path.split("\\"))

print_tree(root)
