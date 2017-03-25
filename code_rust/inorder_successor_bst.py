"""
Inorder Successor BST
"""


def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root


def inorder_successor_bst(root, d):
    if root is None:
        return
    successor = None
    while root:
        if root.data < d:
            root = root.right
        elif root.data > d:
            successor = root
            root = root.left
        else:
            if root.right:
                successor = find_min(root.right)
            break
    return successor
