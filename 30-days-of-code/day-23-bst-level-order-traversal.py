import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        results = []
        queue = []

        # enqueue
        queue.append(root)
        while len(queue):
            # dequeue
            node = queue.pop(0)
            results.append(node.data)

            # enqueue
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        print(" ".join(map(str, results)))
        assert "3 2 5 1 4 7" == " ".join(map(str, results))


myTree = Solution()
root = None
for data in [3, 5, 4, 7, 2, 1]:
    root = myTree.insert(root, data)
myTree.levelOrder(root)
