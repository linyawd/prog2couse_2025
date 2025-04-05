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
