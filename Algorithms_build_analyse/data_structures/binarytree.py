class Node:
    def __init__(self, value, left=None, right=None):
        self.key = value
        self.parent = None
        self.left = left
        self.right = right


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

    def get_max(self):
        x = self.root
        while x.right is not None:
            x = x.right
        return x.key

    def get_min(self):
        x = self.root
        while x.left is not None:
            x = x.left
        return x.key

    def display_tree(self, item: Node, level=0):
        if item is not None:
            self.display_tree(item.left, level + 1)
            print(' ' * 4 * level + '->', item.key)
            self.display_tree(item.right, level + 1)


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
    print(tree.get_min())
    print(tree.get_max())
