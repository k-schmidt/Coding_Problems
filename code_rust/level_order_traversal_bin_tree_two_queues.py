"""
Level Order Traversal of Binary Tree with Two Queues
"""
from collections import deque


def level_order_traversal(root):
    if root is None:
        return

    queues = [deque(), deque()]
    current_queue = queues[0]
    next_queue = queues[1]
    current_queue.append(root)
    level_number = 0

    while current_queue:
        temp = current_queue.popleft()
        print(temp.data, sep=",")
        if temp.left:
            next_queue.append(temp.left)
        if temp.right:
            next_queue.append(temp.right)

        if not current_queue:
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]
