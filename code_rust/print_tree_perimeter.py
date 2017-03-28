"""
Print Tree Perimeter
"""


def print_left_perimeter(root):
    while root is not None:
        curr_val = root.data

        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:  # leaf node
            break
        print(curr_val)


def print_right_perimeter(root):
    r_values = []  # stack for right side values
    while root:
        curr_val = root.data

        if root.right:
            root = root.right
        elif root.left:
            root = root.left
        else:  # leaf node
            break
        r_values.append(curr_val)

    while r_values:
        print(r_values.pop())


def print_leaf_nodes(root):
    if root:
        print_leaf_nodes(root.left)

        if root.left is None and root.right is None:
            print(root.data)

        print_leaf_nodes(root.right)


def display_tree_perimeter(root):
    if root:
        print(root.data)
        print_left_perimeter(root.left)

        if root.left or root.right:
            print_leaf_nodes(root)

        print_right_perimeter(root.right)
