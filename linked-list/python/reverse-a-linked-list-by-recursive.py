# Reverse a linked list by recursive
# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

def reverse(head):
    if head is None or head.next is None:
        return head

    remaining = reverse(head.next)
    head.next.next = head
    head.next = None
    return remaining

if __name__ == '__main__':
    tests = [[1, 2, 3, 4, 5]]

    for tests_itr in tests:
        llist = SinglyLinkedList()

        for llist_item in tests_itr:
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ')  # 5 4 3 2 1
