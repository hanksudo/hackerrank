class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topViewTraverse(root, distance, level, result):
    if root is None:
        return

    # print(f"info: {root.info}, level: {level} {result.get(distance)}")
    if distance not in result or level < result[distance].level:
        root.level = level
        result[distance] = root

    topViewTraverse(root.left, distance - 1, level + 1, result)
    topViewTraverse(root.right, distance + 1, level + 1, result)

def topView(root):
    result = {}
    topViewTraverse(root, 0, 0, result)
    for key in sorted(result):
        print(f"{result[key]}", end=" ")

tests = (
    # [1, 2, 5, 6, 3, 4],
    # [4, 2, 6, 1, 3, 5, 7],
    [37, 23, 108, 59, 86, 64, 94, 14, 105, 17, 111, 65, 55, 31, 79, 97, 78, 25, 50, 22, 66, 46, 104, 98, 81, 90, 68, 40, 103, 77, 74, 18, 69, 82, 41, 4, 48, 83, 67, 6, 2, 95, 54, 100, 99, 84, 34, 88, 27, 72, 32, 62, 9, 56, 109, 115, 33, 15, 91, 29, 85, 114, 112, 20, 26, 30, 93, 96, 87, 42, 38, 60, 7, 73, 35, 12, 10, 57, 80, 13, 52, 44, 16, 70, 8, 39, 107, 106, 63, 24, 92, 45, 75, 116, 5, 61, 49, 101, 71, 11, 53, 43, 102, 110, 1, 58, 36, 28, 76, 47, 113, 21, 89, 51, 19, 3],
)
for test in tests:
    tree = BinarySearchTree()
    for i in test:
        tree.create(i)
    topView(tree.root)
    print()
