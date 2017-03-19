"""
Swap Nth Node with Head
"""


def swap_nth_node(head, n):
    prev = None
    current = head

    if head is None:
        return head

    if n == 1:
        return head

    count = 1
    while current is not None and count < n:
        prev = current
        current = current.next
        count += 1

    if current is None:
        return head

    # Current is pointing to nth node
    # Let's swap nth node with head

    prev.next = head
    temp = head.next
    head.next = current.next
    current.next = temp

    return current
