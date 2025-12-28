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
    def mergeTwoLists(self, list1: Node | None, list2: Node | None) -> Node | None:
        if not (list1 or list2):
            return

        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val > list2.val:
            head = Node(val=list2.val)
            current1 = list1
            current2 = list2.next
        else:
            head = Node(val=list1.val)
            current1 = list1.next
            current2 = list2

        current = head
        while current1 or current2:
            is_current1_smaller = False
            if current1 and current2 and current1.val <= current2.val:
                is_current1_smaller = True
            elif current1 is None and current2 is not None:
                is_current1_smaller = False
            elif current1 is not None and current2 is None:
                is_current1_smaller = True
            val = current1.val if is_current1_smaller else current2.val

            new_node = Node(val=val)
            current.next = new_node
            current = new_node

            current1 = current1.next if is_current1_smaller else current1
            current2 = (
                current2.next
                if (
                    not is_current1_smaller
                    and (current1.val != current2.val if current1 else float("inf"))
                )
                else current2
            )
        return head


if __name__ == "__main__":
    numbers_1 = [
        int(num)
        for num in input("Enter the first list numbers(divide by space): ").split()
    ]
    numbers_2 = [
        int(num)
        for num in input("Enter the second list numbers(divide by space): ").split()
    ]

    l1 = Node(val=numbers_1[0]) if numbers_1 else None
    next_node: Node = l1
    for num in numbers_1[1:]:
        new_node = Node(val=num)
        next_node.next = new_node
        next_node = new_node

    l2 = Node(val=numbers_2[0]) if numbers_2 else None
    next_node: Node = l2
    for num in numbers_2[1:]:
        new_node = Node(val=num)
        next_node.next = new_node
        next_node = new_node

    result = Solution().mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=", ")
        result = result.next
    print("\n")
