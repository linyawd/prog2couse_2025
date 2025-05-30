class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def is_same(a, b):
    if not a and not b:
        return True
    if not a or not b or a.val != b.val:
        return False
    return is_same(a.left, b.left) and is_same(a.right, b.right)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

tree1 = None
for x in a:
    tree1 = insert(tree1, x)

tree2 = None
for x in b:
    tree2 = insert(tree2, x)

print(1 if is_same(tree1, tree2) else 0)
