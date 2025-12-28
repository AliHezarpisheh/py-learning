class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(val=0, next=head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next if slow.next else None
        return dummy.next


if __name__ == "__main__":
    numbers = [int(num) for num in input("Enter numbers: ").split()]
    head = ListNode(val=numbers[0])

    current = head
    for num in numbers[1:]:
        new_node = ListNode(val=int(num))
        current.next = new_node
        current = new_node

    result = Solution().removeNthFromEnd(head=head, n=1)
    while result:
        print(result.val, sep=", ")
        result = result.next
    print("\n")
