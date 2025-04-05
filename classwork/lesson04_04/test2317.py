class Tree:
    def __init__(self, key, parent = None):
        self.key = key
        self.children = []
        self.parent = parent

    def __dfs(self, key):
        if self.key == key:
            return self
        for child in self.children:
            node = child.__dfs(key)
            if node is not None:
                return node
        return None

    def dfs(self, key):
        return self.__dfs(key)

    def add(self, parent_key, key):
        parent = self.dfs(parent_key)
        parent.children.append(Tree(key, parent))

    def lcs(self, i, j):
        node = self.dfs(i)
        while node is not None:
            if node.dfs(j) is not None:
                return node.key
            node = node.parent


if __name__ == "__main__":
    with open("input.txt") as f:
        k = int(f.readline())
        tree = Tree(1)
        for _ in range(k):
            cmd, *args  = f.readline().split()
            a, b = map(int, args)
            if cmd == "ADD":
                tree.add(a, b)
            elif cmd == "GET":
                print(tree.lcs(a, b))