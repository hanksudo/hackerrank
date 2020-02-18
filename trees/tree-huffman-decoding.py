def decodeHuff(root, s):
    node = root
    for c in s:
        if c == "0" and node.left:
            node = node.left
        elif c == "1" and node.right:
            node = node.right

        if node.left is None and node.right is None:
            print(node.data, end="")
            node = root
