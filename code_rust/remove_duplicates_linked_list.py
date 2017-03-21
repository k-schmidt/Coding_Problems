"""
Remove duplicates from linked list
"""


def remove_duplicates(head):
    if head is None:
        return head

    # Track existing values.
    dup_set = set()
    dup_set.add(head.data)
    curr = head

    while curr.next is not None:
        if curr.next.data in dup_set:
            curr.next = curr.next.next
        else:
            dup_set.add(curr.next.data)
            curr = curr.next
    return head
