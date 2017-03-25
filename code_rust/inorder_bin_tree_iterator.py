"""
Write an Inorder Iterator for a Binary Tree
"""


class InorderIterator:
    def __init__(self, root):
        self.stack = []
        # Assuming that when iterator is initialized
        # it is always at the first element of tree in its in-order
        while root:
            self.stack.append(root)
            root = root.left

    def has_next(self):
        if not self.stack:
            return False
        else:
            return True

    def get_next(self):
        """
        get_next returns null if there are no more elements in tree
        """
        if not self.stack:
            return

        r_val = self.stack.pop()
        temp = r_val.right
        while temp:
            self.stack.append(temp)
            temp = temp.left

        return r_val
