# Print Linked List in Reverse
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

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

def reversePrint(head):
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    current = prev
    print(current.data)
    while current.next:
        current = current.next
        print(current.data)
    
if __name__ == '__main__':
    tests = [[16, 12, 4, 2, 5], [7, 3, 9], [5, 1, 18, 3, 13]]
    for tests_itr in tests:
        llist = SinglyLinkedList()

        for llist_item in tests_itr:
            llist.insert_node(llist_item)

        reversePrint(llist.head)

# 5
# 2
# 4
# 12
# 16
# 9
# 3
# 7
# 13
# 3
# 18
# 1
# 5
