class Node:
    def __init__(self, value, left=None, right=None):
        self.key = value
        self.parent = None
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Item with key {self.key}."


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        item = Node(value)
        y = None
        x = self.root

        if x is None:
            self.root = item
        else:
            while x is not None:
                y = x
                if item.key > x.key:
                    x = x.right
                else:
                    x = x.left
            item.parent = y

            if item.key > y.key:
                y.right = item
            else:
                y.left = item

    @classmethod
    def get_max(cls, item: Node):
        x = item
        while x.right is not None:
            x = x.right
        return x

    @classmethod
    def get_min(cls, item: Node):
        x = item
        while x.left is not None:
            x = x.left
        return x

    def get_successor(self, item):
        x = self.search(item)
        if x.right is not None:
            return self.get_min(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def get_predecessor(self, item):
        x = self.search(item)
        if x.left is not None:
            return self.get_max(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def search(self, value):
        x = self.root
        while x is not None and x.key != value:
            if x.key < value:
                x = x.right
            else:
                x = x.left
        return x

    def display_tree(self, item: Node, level=0):
        if item is not None:
            self.display_tree(item.right, level + 1)
            print(' ' * 4 * level + '->', item.key)
            self.display_tree(item.left, level + 1)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(25)
    tree.insert(10)
    tree.insert(40)
    tree.insert(5)
    tree.insert(15)
    tree.insert(35)
    tree.insert(55)
    tree.insert(7)

    tree.display_tree(tree.root)
    print(tree.get_predecessor(35))
