class Node:
    def __init__(self, value: int, left=None, right=None):
        self.key = value
        self.parent = None
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.key == other.key and self.right == other.right and self.left == other.left

    def __repr__(self):
        return f"Item with key {self.key}."


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
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

    def get_successor(self, value: int):
        x = self.search(value)
        if x.right is not None:
            return self.get_min(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def get_predecessor(self, value: int):
        x = self.search(value)
        if x.left is not None:
            return self.get_max(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def search(self, value: int):
        x = self.root
        while x is not None and x.key != value:
            if x.key < value:
                x = x.right
            else:
                x = x.left
        return x

    def _transplant(self, x: Node, y: Node):
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        if y is not None:
            y.parent = x.parent

    def delete_node(self, value: int):
        x = self.search(value)
        if x:
            if x.left is None:
                self._transplant(x, x.right)
            elif x.right is None:
                self._transplant(x, x.left)
            else:
                y = self.get_min(x.right)
                if y.parent != x:
                    self._transplant(y, y.right)
                    y.right = x.right
                    y.right.parent = y

                self._transplant(x, y)
                y.left = x.left
                x.left.parent = y


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
    print()
    tree.delete_node(25)
    tree.display_tree(tree.root)
