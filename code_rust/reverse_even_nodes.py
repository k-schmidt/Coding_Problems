"""
Reverse Even Nodes
"""


def merge_alternating(list1, list2):
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    head = list1
    while list1.next is not None and list2:
        temp = list2
        list2 = list2.next
        temp.next = list1.next
        list1.next = temp
        list1 = temp.next

    if list1.next is None:
        list1.next = list2

    return head


def reverse_even_nodes(head):
    """
    Let's extract even nodes from the existing
    list and create a new list consisting of even nodes.
    We will push the even nodes at head
    since we want them to be in reverse order
    """

    curr = head
    list_even = None
    while curr is not None and curr.next is not None:
        even = curr.next
        curr.next = even.next

        # Push at the head of new list
        even.next = list_even
        list_even = even
        curr = curr.next

    # Now, merge the two lists
    return merge_alternating(head, list_even)
