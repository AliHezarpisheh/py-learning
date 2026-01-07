class MyQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def push(self, x: int) -> None:
        self.inbound_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Queue is empty!")

        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

    def peek(self) -> int:
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack[-1] 

    def empty(self) -> bool:
        if self.inbound_stack or self.outbound_stack:
            return False
        return True
