from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        queue_length = len(self.queue)
        self.queue.append(x)
        for _ in range(queue_length):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Queue is empty!")
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError("Queue is empty!")
        return self.queue[0]

    def empty(self) -> bool:
        return not bool(self.queue)



