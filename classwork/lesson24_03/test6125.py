class Queue:
    def __init__(self, maxsize=100):
        self._items = [None] * maxsize
        self._front = 0
        self._back = 0
        self._size = 0
        self._maxsize = maxsize

    def push(self, n):
        self._items[self._back] = n
        self._back = (self._back + 1) % self._maxsize
        self._size += 1
        print("ok")

    def pop(self):
        res = self._items[self._front]
        self._front = (self._front + 1) % self._maxsize
        self._size -= 1
        print(res)

    def front(self):
        print(self._items[self._front])

    def size(self):
        print(self._size)

    def clear(self):
        self._front = 0
        self._back = 0
        self._size = 0
        print("ok")

def main():
    queue = Queue()
    while True:
        command = input().strip().split()
        if command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()
        elif command[0] == "front":
            queue.front()
        elif command[0] == "size":
            queue.size()
        elif command[0] == "clear":
            queue.clear()
        elif command[0] == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()

