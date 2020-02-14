# Insert a node at a specific position in a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

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
    list_elemenets = []
    while node:
        list_elemenets.append(str(node.data))
        node = node.next

    print(sep.join(list_elemenets))

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)

    if position == 1:
        new_node.next = head
        return new_node

    current = head
    for i in range(position - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node

    return head

if __name__ == '__main__':
    llist = SinglyLinkedList()

    for llist_item in [16, 13, 7]:
        llist.insert_node(llist_item)

    data = 1

    position = 2

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ')  # 16 13 1 7
