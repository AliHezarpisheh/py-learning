"""
Inserting a Node Into a Sorted Doubly Linked List

https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
"""

import os

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    head = llist
    new_node = DoublyLinkedListNode(node_data=data)

    prev = None
    current = llist
    while current:
        if data <= current.data:
            if current.prev:
                current.prev.next = new_node
            else:
                head = new_node

            if current.next:
                current.next.prev = new_node

            new_node.next = current
            new_node.prev = current.prev
            return head
        prev = current
        current = current.next

    prev.next = new_node
    new_node = prev.prev
    return head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print()
        print_doubly_linked_list(llist1, ' ')

