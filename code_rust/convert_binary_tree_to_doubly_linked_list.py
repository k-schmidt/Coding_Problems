"""
Convert Binary Tree to Doubly Linked List
"""


def concatenate_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # use left for previous
    # use right for next
    tail1 = head1.left
    tail2 = head2.left
    tail1.right = head2
    head2.left = tail1
    head1.left = tail2
    tail2.right = head1
    return head1


def convert_to_linked_list(root):
    if root is None:
        return
    list1 = convert_to_linked_list(root.left)
    list2 = convert_to_linked_list(root.right)
    root.left = root.right = root
    result = concatenate_lists(list1, root)
    result = concatenate_lists(result, list2)

    return result
