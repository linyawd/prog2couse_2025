class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, n):
        new_node = Node(n)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print("ok")

    def pop(self):
        if self.top is None:
            print("error")
        else:
            value = self.top.value
            self.top = self.top.next
            self.size -= 1
            print(value)

    def back(self):
        if self.top is None:
            print("error")
        else:
            print(self.top.value)

    def get_size(self):
        print(self.size)

    def clear(self):
        self.top = None
        self.size = 0
        print("ok")

    def exit(self):
        print("bye")
        return

# Основна програма
stack = Stack()
while True:
    command = input().strip().split()
    if not command:
        continue
    if command[0] == "push":
        if len(command) < 2:
            print("error")
        else:
            stack.push(int(command[1]))
    elif command[0] == "pop":
        stack.pop()
    elif command[0] == "back":
        stack.back()
    elif command[0] == "size":
        stack.get_size()
    elif command[0] == "clear":
        stack.clear()
    elif command[0] == "exit":
        stack.exit()
        break
    else:
        print("error")