# Merge two sorted linked lists
# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

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

# Iterative
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    tail = dummy
    while True:
        if head1 is None:
            tail.next = head2
            break
        
        if head2 is None:
            tail.next = head1
            break

        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    return dummy.next

# Recursion
# def mergeLists(head1, head2):
#     if head1 is None:
#         return head2

#     if head2 is None:
#         return head1
    
#     if head1.data <= head2.data:
#         head1.next = mergeLists(head1.next, head2)
#         return head1
#     else:
#         head2.next = mergeLists(head1, head2.next)
#         return head2


if __name__ == '__main__':

    tests = [
        [[1, 2, 3], [3, 4]]
    ]

    for tests_itr in tests:
        llist1 = SinglyLinkedList()

        for llist1_item in tests_itr[0]:
            llist1.insert_node(llist1_item)

        llist2 = SinglyLinkedList()

        for llist2_item in tests_itr[1]:
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
