# Find Merge Point of Two Lists
# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
#
# https://stackoverflow.com/questions/1594061/check-if-two-linked-lists-merge-if-so-where/14956113#14956113
# a - b - d - None
#      c /

"""
C1 C2
a c
b d
d a
c b
d d
"""
def findMergeNode(head1, head2):
    if head1 is None or head2 is None:
        return None

    current1 = head1
    current2 = head2

    while current1 != current2:
        if current1 is None:
            current1 = head2
        else:
            current1 = current1.next

        if current2 is None:
            current2 = head1
        else:
            current2 = current2.next

    return current2.data
