class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None


class List:

    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def _print_reverse(self, node: 'Node | None') -> None:
        if node is None:
            return
        self._print_reverse(node.next)
        print(node.data, end=' ')

    def PrintReverse(self) -> None:
        self._print_reverse(self.head)
        print()


# Зчитування вхідних даних
n = int(input())
values = list(map(int, input().split()))

lst = List()
for val in values:
    lst.addToTail(val)

lst.Print()
lst.PrintReverse()
