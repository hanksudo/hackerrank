# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head is None:
        return node

    currentNode = head
    while currentNode.next:
        currentNode = currentNode.next

    currentNode.next = node
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()

    for llist_item in [141, 302, 164, 530, 474]:
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
    # 141, 302, 164, 530, 474
