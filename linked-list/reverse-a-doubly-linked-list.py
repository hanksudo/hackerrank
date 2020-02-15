# Reverse a doubly linked list
# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

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
    print()

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    while head:
        _next = head.next
        head.next = head.prev
        if _next:
            head.prev = _next
            head = _next
        else:
            head.prev = None
            break
    return head

if __name__ == '__main__':
    tests = [
        [1, 2, 3, 4]
    ]

    for t_itr in tests:
        llist = DoublyLinkedList()

        for llist_item in t_itr:
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ')
