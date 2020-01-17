class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1
        left_depth = self.getHeight(root.left)
        right_depth = self.getHeight(root.right)
        return max(left_depth, right_depth) + 1

myTree = Solution()
root = None
for data in [3, 5, 2, 1, 4, 6, 7]:
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
assert height == 3
