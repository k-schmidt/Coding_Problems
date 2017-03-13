"""
Rank from Stream
"""


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.left_size = 0

    def insert(self, d):
        if d <= self.data:
            if self.left is not None:
                self.left.insert(d)
            else:
                self.left = Node(d)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(d)
            else:
                self.right = Node(d)

    def get_rank(self, d):
        if d == self.data:
            return self.left_size
        elif d < self.data:
            if self.left is None:
                return -1
            else:
                return self.left.get_rank(d)
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(d)
            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank


def track(number, root):
    if root is None:
        root = Node(number)
    else:
        root.insert(number)
