import sys


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        print("ok")

    def pop(self):
        print(self.queue.pop(0) if self.queue else "error")

    def front(self):
        print(self.queue[0] if self.queue else "error")

    def size(self):
        print(len(self.queue))

    def clear(self):
        self.queue.clear()
        print("ok")


q = Queue()
for command in sys.stdin:
    command = command.strip()
    if command.startswith("push"):
        _, n = command.split()
        q.push(int(n))
    elif command == "pop":
        q.pop()
    elif command == "front":
        q.front()
    elif command == "size":
        q.size()
    elif command == "clear":
        q.clear()
    elif command == "exit":
        print("bye")
        break
