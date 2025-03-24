from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def push_front(self, x):
        self.deque.appendleft(x)
        print("ok")

    def push_back(self, x):
        self.deque.append(x)
        print("ok")

    def pop_front(self):
        print(self.deque.popleft())

    def pop_back(self):
        print(self.deque.pop())

    def front(self):
        print(self.deque[0])

    def back(self):
        print(self.deque[-1])

    def size(self):
        print(len(self.deque))

    def clear(self):
        self.deque.clear()
        print("ok")

    def exit(self):
        print("bye")
        exit()


d = Deque()
while True:
    command = input().split()
    if command[0] == "push_front":
        d.push_front(int(command[1]))
    elif command[0] == "push_back":
        d.push_back(int(command[1]))
    elif command[0] == "pop_front":
        d.pop_front()
    elif command[0] == "pop_back":
        d.pop_back()
    elif command[0] == "front":
        d.front()
    elif command[0] == "back":
        d.back()
    elif command[0] == "size":
        d.size()
    elif command[0] == "clear":
        d.clear()
    elif command[0] == "exit":
        d.exit()