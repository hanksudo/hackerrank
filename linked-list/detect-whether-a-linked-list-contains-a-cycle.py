# Cycle Detection
# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/forum/comments/135314
def has_cycle(head):
    if head is None:
        return 0

    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1

    return 0
