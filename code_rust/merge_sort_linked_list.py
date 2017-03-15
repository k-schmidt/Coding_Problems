"""
Merge Sort Linked List
"""


# This method splits linked list in two halves by iterating over whole list
# It returns head pointers of first and 2nd halves of linked lists in first_second
# Head of 1st half is just the head node of linked list
def split_in_half(head, first_second):

    if head is None:

        first_second.first = None
        first_second.second = None
        return

    # Only one element in the list
    if head.next is None:

        first_second.first = head
        first_second.second = None
    else:

        # Let's use the classic technique of moving two pointers:
        # 'fast' and 'slow'. 'fast' will move two steps in each
        # iteration where 'slow' will be pointing to middle element
        # at the end of loop.
        slow = head
        fast = head.next

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next

        first_second.first = head
        first_second.second = slow.next

        # Terminate first linked list.
        slow.next = None


def merge_sorted_lists(first, second):

    if first is None:
        return second

    if second is None:
        return first

    new_head = None

    if first.data <= second.data:

        new_head = first
        first = first.next
    else:

        new_head = second
        second = second.next

    new_current = new_head
    while first is not None and second is not None:
        temp = None
        if first.data <= second.data:
            temp = first
            first = first.next
        else:
            temp = second
            second = second.next

        new_current.next = temp
        new_current = temp

    if first is not None:
        new_current.next = first
    elif second is not None:
        new_current.next = second

    return new_head


def merge_sort(head):

    # No need to sort a single element.
    if head is None or head.next is None:
        return head

    first_second = (None, None)

    # Let's split the list in half, sort the sublists
    # and then merge the sorted lists.
    split_in_half(head, first_second)

    first_second.first = merge_sort(first_second.first)
    first_second.second = merge_sort(first_second.second)

    return merge_sorted_lists(first_second.first, first_second.second)
