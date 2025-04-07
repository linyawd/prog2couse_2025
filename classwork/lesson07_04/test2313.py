class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key == node.key:
                return
            elif key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = SearchTree(key)
                    return
                else:
                    node = node.right

    def count_elements(self):
        count = 0
        stack = [self]
        while stack:
            node = stack.pop()
            count += 1
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return count


if __name__ == '__main__':
    l = [int(x) for x in input().split()]
    if l[0] == 0:
        print(0)
        exit()
    tree = SearchTree(l[0])
    i = 1
    while i < len(l) and l[i] != 0:
        tree.insert(l[i])
        i += 1
    print(tree.count_elements())