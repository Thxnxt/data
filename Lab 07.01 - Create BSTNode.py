"""d"""


class BSTNode:
    """d"""

    def __init__(self, data):
        """d"""
        self.data = data
        self.right = None
        self.left = None

    def set_data(self, data):
        """D"""
        self.data = data

    def get_data(self):
        """D"""
        return self.data

    def set_left(self, left):
        """d"""
        self.left = left

    def get_left(self):
        """D"""
        return self.left

    def set_right(self, right):
        """D"""
        self.right = right

    def get_right(self):
        """d"""
        return self.right


BST_ = BSTNode(int(input()))
print(BST_.get_data())
print(BST_.get_left())
print(BST_.get_right())
