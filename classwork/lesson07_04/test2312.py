class Node:
    __slots__ = ['value', 'left', 'right']
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                break
            current = current.right
        else:
            break
    return root

def height(root):
    if root is None:
        return 0
    stack = [(root, 1)]
    max_height = 0
    while stack:
        node, current_height = stack.pop()
        if current_height > max_height:
            max_height = current_height
        if node.left:
            stack.append((node.left, current_height + 1))
        if node.right:
            stack.append((node.right, current_height + 1))
    return max_height

numbers = list(map(int, input().split()))
root = None
for num in numbers:
    if num == 0:
        break
    root = insert(root, num)

print(height(root))
