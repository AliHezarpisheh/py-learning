class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        counter = 0
        while fast:
            if fast == slow:
                return True

            fast = fast.next
            slow = slow.next if counter % 2 == 1 else slow
            counter += 1 

        return False
