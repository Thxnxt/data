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

class BST:
    """tree"""
    def __init__(self):
        """d"""
        self.root = None

    def get_root(self):
        """d"""
        return self.root

    def set_root(self, root):
        """d"""
        self.root = root

    def insert(self, data):
        """d"""
        new = BSTNode(data)
        check = self.get_root()
        if self.root == None:
            self.root = new
        else:
            while True:
                if data < check.get_data():
                    if check.get_left() == None:
                        check.set_left(new)
                        break
                    check = check.get_left()
                elif data >= check.get_data():
                    if check.get_right() == None:
                        check.set_right(new)
                        break
                    check = check.get_right()
    def is_empty(self):
        """d"""
        return self.root == None

    def preorder(self, root=None):
        """d"""
        if root != None:
            print("->", root.get_data(), end=" ")
            if root.get_left() != None:
                self.preorder(root.get_left())
            if root.get_right() != None:
                self.preorder(root.get_right())
        else:
            root = self.get_root()
            self.preorder(root)

    def inorder(self, root=None):
        """f"""
        if root is None:
            root = self.get_root()

        if root is not None:
            if root.get_left() is not None:
                self.inorder(root.get_left())
            print("->", root.get_data(), end=" ")
            if root.get_right() is not None:
                self.inorder(root.get_right())

    def postorder(self, root=None):
        """d"""
        if root is None:
            root = self.get_root()

        if root is not None:
            if root.get_left() is not None:
                self.postorder(root.get_left())
            if root.get_right() is not None:
                self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")

    def traverse(self):
        """d"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end="")
        self.preorder()
        print("\nInorder: ", end="")
        self.inorder()
        print("\nPostorder: ", end="")
        self.postorder()

def main():
    """d"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
main()
