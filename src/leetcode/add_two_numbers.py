class Node:
    def __init__(self, val: int = 0, next: "Node" = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Return the string representation of the class."""
        return f"{self.__class__.__name__}<data: {self.val}>"

    def __repr__(self) -> str:
        """Return the official string representation of the class."""
        return f"{self.__class__.__name__}(data={self.val})"


class Solution:
    def add_two_numbers(self, l1: Node | None, l2: Node | None) -> Node | None:
        if (l1 is None) and (l2 is None):
            return None

        next_node: Node | None = None

        carry = 0
        current_l1_node = l1
        current_l2_node = l2
        while current_l1_node or current_l2_node or carry:
            total_sum = (
                (current_l1_node.val if current_l1_node else 0)
                + (current_l2_node.val if current_l2_node else 0)
                + carry
            )
            new_val = total_sum % 10
            carry = 1 if total_sum > 9 else 0

            new_node = Node(val=new_val)
            new_node.next = next_node

            next_node = new_node
            current_l1_node = current_l1_node.next if current_l1_node else None
            current_l2_node = current_l2_node.next if current_l2_node else None

        return self.revers_nodes(new_node)

    @staticmethod
    def revers_nodes(node: Node) -> Node:
        prev = None
        current = node

        while current is not None:
            old_next = current.next

            current.next = prev

            prev = current
            current = old_next
        return prev


if __name__ == "__main__":
    numbers_1 = [
        int(num)
        for num in input("Enter the first list numbers(divide by space): ").split()
    ]
    numbers_2 = [
        int(num)
        for num in input("Enter the second list numbers(divide by space): ").split()
    ]

    l1 = Node(val=numbers_1[0])
    next_node: Node = l1
    for num in numbers_1[1:]:
        new_node = Node(val=num)
        next_node.next = new_node
        next_node = new_node

    l2 = Node(val=numbers_2[0])
    next_node: Node = l2
    for num in numbers_2[1:]:
        new_node = Node(val=num)
        next_node.next = new_node
        next_node = new_node

    result = Solution().add_two_numbers(l1=l1, l2=l2)
    while result:
        print(result.val, end=", ")
        result = result.next
    print("\n")
