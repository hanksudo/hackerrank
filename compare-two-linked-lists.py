# Compare two linked lists
# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

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

def compare_lists(head1, head2):
    while head1 is not None and head2 is not None:
        if head1.data != head2.data:
            return 0
        
        head1 = head1.next
        head2 = head2.next
    
    if (head1 is None or head2 is None) and head1 != head2:
        return 0
    
    return 1

# Recursive
# def compare_lists(head1, head2):
#     if head1 is None and head2 is None:
#         return 1
#     elif head1 is None or head2 is None or head1.data != head2.data:
#         return 0
    
#     return compare_lists(head1.next, head2.next)

if __name__ == '__main__':
    tests = [
        [
            [1, 2], [1]
        ], [
            [1, 2], [1, 2]
        ]
    ]

    for tests_itr in tests:
        llist1 = SinglyLinkedList()

        for llist1_item in tests_itr[0]:
            llist1.insert_node(llist1_item)
            
        llist2 = SinglyLinkedList()

        for llist2_item in tests_itr[1]:
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)
        print(result)
# 0
# 1
