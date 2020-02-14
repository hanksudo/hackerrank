# Get Node Value
# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

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

def getNode(head, positionFromTail):
    current = head
    stack = [current.data]
    while current:
        stack.append(current.data)
        current = current.next
    
    return stack[-(positionFromTail + 1)]

if __name__ == '__main__':
    tests = [
        ([1], 0),
        ([3, 2, 1], 2)
    ]

    for tests_itr, position in tests:
        llist = SinglyLinkedList()

        for llist_item in tests_itr:
            llist.insert_node(llist_item)

        result = getNode(llist.head, position)

        print(str(result))
# 1
# 3
