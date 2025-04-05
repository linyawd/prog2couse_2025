class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def RotateRight(self, k):
        if not self.head or k == 0:
            return
        length = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            length += 1
        k %= length
        if k == 0:
            return
        curr.next = self.head
        steps = length - k
        prev = None
        curr = self.head
        for _ in range(steps):
            prev = curr
            curr = curr.next
        prev.next = None
        self.head = curr
        while curr.next:
            curr = curr.next
        self.tail = curr

    def Print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

n = int(input())
vals = input().split()
lst = List()
for val in vals:
    lst.addToTail(int(val))
try:
    while True:
        k = int(input())
        lst.RotateRight(k)
        lst.Print()
except EOFError:
    pass
