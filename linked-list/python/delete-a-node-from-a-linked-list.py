# Delete a Node
# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

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

def deleteNode(head, position):
    if position == 0:
        return head.next
    
    current = head
    for _ in range(position - 1):
        current = current.next
    
    current.next = current.next.next
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()

    for llist_item in [20, 6, 2, 19, 7, 4, 15, 9]:
        llist.insert_node(llist_item)

    position = 3

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ')  # 20 6 2 7 4 15 9
