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

    def append_head(self, item):
        new_item = NodeList(item)
        if self.is_empty():
            self._head = new_item
            self._tail = new_item
        else:
            new_item.next = self._head
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
            iteration = iter(self)
            current_item = next(iteration)
            prev_item = None
            while index > 0:
                prev_item = current_item
                current_item = next(iteration)
                index -= 1

            prev_item.next = new_item
            new_item.next = current_item
            self._lenght += 1


    def __len__(self):
        return self._lenght

    def __str__(self):
        return " --> ".join([str(item) for item in self])

    def __iter__(self):
        current_item = self._head
        while current_item:
            yield current_item
            current_item = current_item.next


if __name__ == '__main__':
    my_llist = SLinkedList()
    print(my_llist.is_empty())
    # for i in range(10):
    #     my_llist.append_tail(i)
    print(my_llist)
    my_llist.append_position('test', 0)
    my_llist.append_position('test2', 1)
    my_llist.append_position('test3', 2)
    print(my_llist)