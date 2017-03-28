"""
Connect Same Level Siblings
"""


def connect_next_level(head):
    current = head
    next_level_head = None
    prev = None

    while current:
        if current.left and current.right:
            if next_level_head is None:
                next_level_head = current.left

            current.left.next = current.right

            if prev:
                prev.next = current.next

            prev = current.right
        elif current.left:
            if next_level_head is None:
                next_level_head = current.left

            if prev:
                prev.next = current.left
            prev = current.left
        elif current.right:
            if next_level_head is None:
                next_level_head = current.right
            if prev:
                prev.next = current.right

            prev = current.right

        current = current.next
    if prev:
        prev.next = None
    return next_level_head


def populate_sibling_pointers(root):
    if root is None:
        return
    root.next = None
    while root:
        root = connect_next_level(root)
