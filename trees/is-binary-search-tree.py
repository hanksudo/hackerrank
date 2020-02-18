""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

nodes = []

def inorder_traverse(node):
    if node is None:
        return
    inorder_traverse(node.left)
    nodes.append(node)
    inorder_traverse(node.right)

def check_binary_search_tree_(root):
    inorder_traverse(root)
    for i in range(1, len(nodes)):
        if nodes[i].data <= nodes[i - 1].data:
            return False
    return True
