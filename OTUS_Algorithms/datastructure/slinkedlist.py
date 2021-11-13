class NodeList:
    def __init__(self, value):
        self._value = value
        self.next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)


class SLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._lenght = 0

    def is_empty(self):
        return self._head is None

    def append_tail(self, item):
        new_item = NodeList(item)
        if self.is_empty():
            self._head = new_item
            self._tail = new_item
        else:
            self._tail.next = new_item
            self._tail = new_item
        self._lenght += 1

    def __len__(self):
        return self._lenght


