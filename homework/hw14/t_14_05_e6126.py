class RecursiveQueue:
    def __init__(self):
        self.queue = None

    def push(self, n):
        if self.queue is None:
            self.queue = (n, None)
        else:
            front, rest = self.queue
            if rest is None:
                self.queue = (front, (n, None))
            else:
                new_rest = self._push_to_rest(rest, n)
                self.queue = (front, new_rest)

    def _push_to_rest(self, rest_queue, n):
        if rest_queue is None:
            return (n, None)
        current, next_rest = rest_queue
        new_next = self._push_to_rest(next_rest, n)
        return (current, new_next)

    def pop(self):
        if self.queue is None:
            return "error"
        front, rest = self.queue
        self.queue = rest if rest is not None else None
        return front

    def front(self):
        if self.queue is None:
            return "error"
        front, _ = self.queue
        return front

    def size(self):
        return self._count_elements(self.queue)

    def _count_elements(self, queue_part):
        if queue_part is None:
            return 0
        _, rest = queue_part
        return 1 + self._count_elements(rest)

    def clear(self):
        self.queue = None
        return "ok"

if __name__ == "__main__":
    rq = RecursiveQueue()
    while True:
        command = input().split()
        if not command:
            continue
        if command[0] == "push":
            rq.push(int(command[1]))
            print("ok")
        elif command[0] == "pop":
            print(rq.pop())
        elif command[0] == "front":
            print(rq.front())
        elif command[0] == "size":
            print(rq.size())
        elif command[0] == "clear":
            print(rq.clear())
        elif command[0] == "exit":
            print("bye")
            break