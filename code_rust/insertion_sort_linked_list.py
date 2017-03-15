"""
Insertion Sort of a Linked List
"""


def sorted_insert(head, node):
    if node is None:
        return head

    if head is None or node.data <= head.data:
        node.next = head
        return node

    curr = head
    while curr.next is not None and curr.next.data < node.data:
        curr = curr.next

    node.next = curr.next
    curr.next = node

    return head


def insertion_sort(head):
    sorted = None
    curr = head

    while curr is not None:
        temp = curr.next
        sorted = sorted_insert(sorted, curr)
        curr = temp

    return sorted
