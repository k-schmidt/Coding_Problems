"""
Connect All Siblings
"""
from collections import deque


def populate_sibling_pointers(root):
    if root is None:
        return

    current = root
    last = root

    while current:
        if current.left:
            last.next = current.left
            last = current.left

        if current.right:
            last.next = current.right
            last = current.right
        last.next = None
        current = current.next


def populate_sibling_pointers_2(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    prev = None

    while queue:
        temp = queue.popleft()

        if prev:
            prev.next = temp

        prev = temp

        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    prev.next = None
