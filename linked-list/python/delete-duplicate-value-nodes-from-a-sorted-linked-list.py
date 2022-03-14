# Delete duplicate-value nodes from a sorted linked list
# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

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
    print()

def concat_linked_list(node, sep=" "):
    values = []
    values.append(node.data)
    while node.next:
        node = node.next
        values.append(node.data)

    return sep.join(map(str, values))

def removeDuplicates(head):
    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

if __name__ == '__main__':
    tests = [
        [1, 2, 2, 3, 4],
        [3, 3, 3, 4, 5, 5]
    ]

    for tests_itr in tests:
        expected = " ".join(map(str, sorted(set(tests_itr))))
        llist = SinglyLinkedList()

        for llist_item in tests_itr:
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ')  # 1 2 3 4
        assert concat_linked_list(llist1) == expected
