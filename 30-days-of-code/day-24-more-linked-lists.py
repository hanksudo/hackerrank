# Day 24: More Linked Lists
# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while(start.next is not None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head

        if head.data == head.next.data:
            head.next = head.next.next
            self.removeDuplicates(head)
        else:
            self.removeDuplicates(head.next)
        
        return head

mylist = Solution()

head = None
for data in [1, 2, 2, 3, 3, 4]:
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
