class PrefixTree:
    def __init__(self):
        self.children: dict[int: PrefixTree] = {}

    def has_child(self, d):
        return d in self.children

    def add_child(self, d):
        self.children[d] = PrefixTree()

    def get_child(self, d):
        return self.children[d]

    def is_leaf(self):
        return len(self.children) == 0

    def add_phone(self, phone:str) -> bool:
        node = self
        i = 0
        while i < len(phone) and node.has_child(phone[i]):
            node = node.get_child(phone[i])
            i += 1

        if i == len(phone):
            return False

        if i > 0 and node.is_leaf():
            return False

        while i < len(phone):
            node.add_child(phone[i])
            node = node.get_child(phone[i])
            i += 1
        return True

if __name__ == "__main__":
    with open("input.txt") as file:
        t = int(file.readline())
        for _ in range(t):
            tree = PrefixTree()
            n = int(file.readline())
            ok = True
            for __ in range(n):
                phone  = file.readline().strip()
                if ok:
                    ok = tree.add_phone(phone)
            if ok:
                print("YES")
            else:
                print("NO")