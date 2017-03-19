"""
Reverse Linked List
"""


def reverse_iterative(head):
    # No need to reverse if head is null
    # Or there is only 1 node.
    if head is None or head.next is None:
        return head
    list_to_do = head.next
    reversed_list = head
    reversed_list.next = None
    while list_to_do is not None:
        temp = list_to_do
        list_to_do = list_to_do.next

        temp.next = reversed_list
        reversed_list = temp

    return reversed_list


def reverse_recursive(head):
    # No need to reverse if head is null
    # or there is only 1 node.
    if head is None or head.next is None:
        return head

    reversed_list = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return reversed_list
