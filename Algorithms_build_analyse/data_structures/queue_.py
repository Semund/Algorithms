import linkedlist


class QueueByStacks:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push(self, item):
        self._stack1.append(item)

    def pop(self):
        if len(self._stack2):
            return self._stack2.pop()
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            return self._stack2.pop()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._stack1) + len(self._stack2)

    def __str__(self):
        return " -> ".join(map(str, self._stack1[::-1] + self._stack2))


class QueueByLinkedList:
    def __init__(self):
        self._queue = linkedlist.SLinkedList()

    def push(self, item):
        self._queue.append_tail(item)

    def pop(self):
        return self._queue.pop_head()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return " -> ".join([str(item) for item in self._queue][::-1])