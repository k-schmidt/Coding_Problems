"""
Intersection Point of Two Lists
"""


def intersect(head1, head2):
    list1node = None
    list1length = get_length(head1)
    list2node = None
    list2length = get_length(head2)

    length_difference = 0
    if list1length >= list2length:
        length_difference = list1length - list2length
        list1node = head1
        list2node = head2
    else:
        length_difference = list2length - list1length
        list1node = head2
        list2node = head1

    while length_difference > 0:
        list1node = list1node.next
        length_difference -= 1

    while list1node is not None:
        if list1node == list2node:
            return list1node

        list1node = list1node.next
        list2node = list2node.next
    return None


def get_length(head):
    list_length = 0
    while head is not None:
        head = head.next
        list_length += 1
    return list_length
