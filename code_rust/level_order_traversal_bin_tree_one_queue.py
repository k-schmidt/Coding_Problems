"""
Level Order Traversal of Binary Tree One Queue
"""
from collections import queue


def level_order_traversal(root):
    if root is None:
        return

    current_queue = deque()
    current_queue.append(root)
    current_queue.append(None)
    while current_queue:
        temp = current_queue.popleft()
        print(temp.data, sep=",")
        if temp.left:
            current_queue.append(temp.left)
        if temp.right:
            current_queue.append(temp.right)

        if current_queue[0] is None:
            print()
            current_queue.popleft()

            if current_queue:
                current_queue.append(None)
    print()
