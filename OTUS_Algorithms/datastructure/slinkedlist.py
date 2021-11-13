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

    def __str__(self):
        return " --> ".join([str(item) for item in self])

    def __iter__(self):
        self.current_item = None
        return self

    def __next__(self):
        if self.current_item is None:
            self.current_item = self._head
        else:
            self.current_item = self.current_item.next
        if self.current_item is None:
            raise StopIteration
        return self.current_item


if __name__ == '__main__':
    my_llist = SLinkedList()
    my_llist.append_tail(9)
    my_llist.append_tail(1)
    my_llist.append_tail(5)
    my_llist.append_tail(2)
    my_llist.append_tail(6)
    print(my_llist)
