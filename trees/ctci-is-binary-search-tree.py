""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

from math import inf
def validateBST(node, min_value, max_value):
    if node is None:
        return True

    return (
        node.data > min_value and
        node.data < max_value and
        validateBST(node.left, min_value, node.data) and
        validateBST(node.right, node.data, max_value)
    )

def checkBST(root):
    return validateBST(root, -inf, inf)
