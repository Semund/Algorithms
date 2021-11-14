class NodeList:
    def __init__(self, value):
        self._value = value
        self.next = None
        self.prev = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)


class DLinkedList:
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
            new_item.prev = self._tail
            self._tail = new_item
        self._lenght += 1

    def append_head(self, item):
        new_item = NodeList(item)
        if self.is_empty():
            self._head = new_item
            self._tail = new_item
        else:
            new_item.next = self._head
            self._head.prev = new_item
            self._head = new_item
        self._lenght += 1

    def append_position(self, item, index):
        if index > self._lenght:
            raise IndexError

        if index == 0:
            self.append_head(item)
        elif index == self._lenght:
            self.append_tail(item)
        else:
            new_item = NodeList(item)

            if index < self._lenght // 2:
                iteration = iter(self)
            else:
                iteration = iter(reversed(self))
                index = self._lenght - index - 1

            current_item = next(iteration)

            while index > 0:
                current_item = next(iteration)
                index -= 1

            prev_item = current_item.prev
            prev_item.next = new_item
            new_item.prev = prev_item
            new_item.next = current_item
            current_item.prev = new_item
            self._lenght += 1


    def __len__(self):
        return self._lenght

    def __str__(self):
        return " <---> ".join([str(item) for item in self])

    def __iter__(self):
        current_item = self._head
        while current_item:
            yield current_item
            current_item = current_item.next

    def __reversed__(self):
        current_item = self._tail
        while current_item:
            yield current_item
            current_item = current_item.prev


if __name__ == '__main__':
    my_llist = DLinkedList()
    for i in range(10):
        my_llist.append_tail(i)
    print(my_llist)
    my_llist.append_position('test', 9)
    print(my_llist)
