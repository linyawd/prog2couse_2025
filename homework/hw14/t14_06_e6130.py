class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, value):
        new_node = Node(value, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self._size += 1
        return "ok"

    def push_back(self, value):
        new_node = Node(value, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if not self.head:
            return "error"
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return value

    def pop_back(self):
        if not self.tail:
            return "error"
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return value

    def front(self):
        if not self.head:
            return "error"
        return self.head.value

    def back(self):
        if not self.tail:
            return "error"
        return self.tail.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

def main():
    deque = Deque()
    while True:
        command = input().split()
        if not command:
            continue
        if command[0] == "push_front":
            print(deque.push_front(int(command[1])))
        elif command[0] == "push_back":
            print(deque.push_back(int(command[1])))
        elif command[0] == "pop_front":
            print(deque.pop_front())
        elif command[0] == "pop_back":
            print(deque.pop_back())
        elif command[0] == "front":
            print(deque.front())
        elif command[0] == "back":
            print(deque.back())
        elif command[0] == "size":
            print(deque.size())
        elif command[0] == "clear":
            print(deque.clear())
        elif command[0] == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()