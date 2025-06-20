class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def Insert(self, val: int) -> None:
        if not self.head:
            self.head = TreeNode(val)
            return
        cur = self.head
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return

    def SumLeft(self) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(self.head, False)

# Головна частина програми
n = int(input())
values = list(map(int, input().split()))

tree = Tree()
for val in values:
    tree.Insert(val)

print(tree.SumLeft())
