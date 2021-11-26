from maxheap import MaxHeap


class Item:
    def __init__(self, values):
        self._key, *self._value = values

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return f"{self.key} --> {','.join(map(str, self._value))}"


class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def insert(self, item):
        item = Item(item)
        self.queue.insert(item)

    def get_max(self):
        return self.queue.get_max()

    def extract_max(self):
        return self.queue.extract_max()

    def increase_key(self, index, priority):
        self.queue.change_priority(index, priority)

    def __len__(self):
        return self.queue.size


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

    while my_queue:
        print(my_queue.extract_max())
