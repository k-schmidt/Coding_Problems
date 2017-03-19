"""
Delete node with a given key
"""


def delete_node(head, key):
    previous = None
    current = head

    while current is not None:
        if current.data == key:
            break
        previous = current
        current = current.next

    # key not found in list
    if current is None:
        return head

    if current == head:
        return current.next

    # for all other cases
    previous.next = current.next

    return head
