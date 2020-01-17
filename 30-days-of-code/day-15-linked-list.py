class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)
        if head is None:
            return node

        current = head
        while True:
            if current.next is None:
                current.next = node
                return head
            current = current.next


mylist = Solution()
T = [2, 3, 4, 1]
head = None
for data in T:
    head = mylist.insert(head, data)
mylist.display(head)
