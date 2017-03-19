"""
Merge Two Sorted Linked Lists
"""


def merge_sorted(head1, head2):
    # if both lists are empty then merged list is also empty
    # if one of the lists is empty then other is the merged list
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    merged_head = None
    if head1.data <= head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next

    merged_tail = merged_head
    while head1 is not None and head2 is not None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        merged_tail.next = temp
        merged_tail = temp

    if head1 is not None:
        merged_tail.next = head1
        merged_tail = head1
    elif head2 is not None:
        merged_tail.next = head2
        merged_tail = head2

    return merged_head
