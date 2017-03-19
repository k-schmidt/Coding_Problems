"""
Remove duplicates from linked list
"""


def remove_duplicates(head):
    if head is None:
        return head

    # Track existing values.
    dup_set = set()
    curr = head
    while curr is not None:
        if curr.data not in dup_set:
            dup_set.add(curr.data)
        curr = curr.next
    return head
