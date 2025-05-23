"""
Merge two sorted linked lists

https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
"""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data), end="\n")
        node = node.next


def mergeLists(head1, head2):
    items = []
    current_list1 = head1
    current_list2 = head2
    while current_list1:
        items.append(current_list1.data)
        current_list1 = current_list1.next

    while current_list2:
        items.append(current_list2.data)
        current_list2 = current_list2.next

    items.sort()

    sll = SinglyLinkedList()
    for item in items:
        sll.insert_node(node_data=item)
    return sll.head


def mergeListsOptimized(head1, head2):
    pointer1 = head1
    pointer2 = head2

    sll = SinglyLinkedList()
    while (pointer1 is not None) and (pointer2 is not None):
        if pointer1.data <= pointer2.data:
            sll.insert_node(pointer1.data)
            pointer1 = pointer1.next
        else:
            sll.insert_node(pointer2.data)
            pointer2 = pointer2.next

    if pointer1 is not None:
        sll.tail.next = pointer1
    elif pointer2 is not None:
        sll.tail.next = pointer2

    return sll.head


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeListsOptimized(llist1.head, llist2.head)

        print("----------")
        print_singly_linked_list(llist3)
