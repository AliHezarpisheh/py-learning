from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.previous = None
