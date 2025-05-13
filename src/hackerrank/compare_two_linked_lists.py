"""
Compare two linked lists

https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def compare_lists(llist1: SinglyLinkedListNode, llist2: SinglyLinkedListNode) -> int:
    current_node_llist1 = llist1
    current_node_llist2 = llist2
    while current_node_llist1:
        if not current_node_llist2:
            return 0

        if current_node_llist1.data != current_node_llist2.data:
            return 0
        current_node_llist1 = current_node_llist1.next
        current_node_llist2 = current_node_llist2.next

    if current_node_llist2:
        return 0

    return 1


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

        result = compare_lists(llist1.head, llist2.head)

        print(str(int(result)) + '\n')
