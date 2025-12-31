from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Return the string representation of the class."""
        return f"{self.__class__.__name__}<data: {self.val}>"

    def __repr__(self) -> str:
        """Return the official string representation of the class."""
        return f"{self.__class__.__name__}(data={self.val})"


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Special case - when list is empty.
        if not lists:
            return None

        # Recursion case
        if len(lists) > 2:
            half = len(lists) // 2

            list1 = self.mergeKLists(lists=[*lists[:half]])
            list2 = self.mergeKLists(lists=[*lists[half:]])
            return self.mergeKLists(lists=[list1, list2])

        # Base cases
        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            list1 = lists[0]
            list2 = lists[1]

            if not list1:
                return list2

            if not list2:
                return list1

            if list1.val > list2.val:
                head = ListNode(val=list2.val)
                current1 = list1
                current2 = list2.next
            else:
                head = ListNode(val=list1.val)
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

                new_node = ListNode(val=val)
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
    lists = []

    lists_count = int(input("Type how many lists you want to insert: "))

    for _ in range(lists_count):
        numbers = [
            int(num)
            for num in input("Enter the second list numbers(divide by space): ").split()
        ]
        l = ListNode(val=numbers[0]) if numbers else None
        next_node: ListNode = l
        for num in numbers[1:]:
            new_node = ListNode(val=num)
            next_node.next = new_node
            next_node = new_node
        lists.append(l)

    result = Solution().mergeKLists(lists=lists)
    while result:
        print(result.val, end=", ")
        result = result.next
    print("\n")
