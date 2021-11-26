from maxheap import MaxHeap


class Item:
    def __init__(self, index, value):
        self._key, *self._value = value
        self.index = index

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key

    def __gt__(self, other):
        return self.key > other.key or (self.key == other.key and self.index < other.index)

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return f"{self.key} --> {','.join(map(str, self._value))}"


class PriorityQueue(MaxHeap):
    def __init__(self):
        super(PriorityQueue, self).__init__()

    def insert(self, item):
        element = Item(self.size, item)
        self.heap.append(element)
        self.size += 1
        self.sift_up(self.size - 1)

    def __len__(self):
        return self.size


if __name__ == '__main__':

    my_queue = PriorityQueue()
    my_queue.insert((1, "tra1"))
    my_queue.insert((2, "tra2"))
    my_queue.insert((3, "tra3"))
    my_queue.insert((3, "tra4"))
    my_queue.insert((1, "tra6"))
    my_queue.insert((3, "tra7"))
    my_queue.insert((2, "tra8"))
    my_queue.insert((1, "tra9"))
    my_queue.insert((2, "tra10"))
    my_queue.insert((3, "tra11"))

    while len(my_queue) != 0:
        print(my_queue.extract_max())
