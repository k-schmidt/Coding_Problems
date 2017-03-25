"""
Iterative Inorder Traversal
"""


def inorder_iterative(root):
    if root is None:
        return

    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            print(node.data)
            root = node.right
