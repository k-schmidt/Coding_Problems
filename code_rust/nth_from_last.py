"""
Nth from Last Node
"""


def find_nth_from_last(head, n):
    if head is None or n < 1:
        return

    # We will use two pointers head and tail
    # where head and tail are 'n' nodes apart.
    tail = head
    while tail is not None and n > 0:
        tail = tail.next
        n -= 1

    # Check if out of bounds
    if n != 0:
        return

    # When tail pointer reaches the end of
    # list, head is pointing at nth node.
    while tail is not None:
        tail = tail.next
        head = head.next

    return head
