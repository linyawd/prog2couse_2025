class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key == 0:
            return
        node = self
        while True:
            if node.key < key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break;
                node = node.right
            elif node.key > key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break;
                node = node.left
            else:
                break;

    def print_(self):
        if self.left is not None:
            self.left.print_()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print_()

    def sizeof(self):
        stack = [self]
        size_t = 0
        while stack:
            node = stack.pop()
            size_t += 1
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return size_t

    def maximum(self):
        q = []
        q.append(tree)

        elements = []

        while q:
            current = q.pop(-1)
            elements.append(current.key)

            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)

        return sorted(elements)[-2]


if __name__ == "__main__":
    lst = [int(x) for x in input().split()]
    # print(sorted(list(set(lst)))[-2] if lst[0] != 0 else 0)
    if lst[0] == 0:
        print(0)
        exit(0)
    else:
        tree = SearchTree(lst[0])
    for i in range(1, len(lst)):
        if lst[i] == 0:
            break;
        tree.insert(lst[i])

    print(tree.maximum())

    