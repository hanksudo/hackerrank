""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

from math import inf
def validateBST(root, min_value, max_value):
    if root is None:
        return True

    return (
        root.data > min_value and
        root.data < max_value and
        validateBST(root.left, min_value, root.data) and
        validateBST(root.right, root.data, max_value)
    )

def checkBST(root):
    return validateBST(root, -inf, inf)
