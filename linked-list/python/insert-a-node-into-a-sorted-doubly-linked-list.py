# Inserting a Node Into a Sorted Doubly Linked List
# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

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
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if node.data < head.data:
        head.prev = node
        node.next = head
        head = node
        return head

    current = head
    while current.next:
        current = current.next
        if node.data < current.data:
            current.prev.next = node
            current.prev = node
            node.next = current
            node.prev = current.prev
            return head

    if current.next is None:
        current.next = node
        node.prev = current

    return head

if __name__ == '__main__':
    tests = [
        ([1, 3, 4, 10], 5),
        ([1, 2, 3], 4)
    ]

    for t_itr, data in tests:
        llist = DoublyLinkedList()

        for llist_item in t_itr:
            llist.insert_node(llist_item)

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ')
