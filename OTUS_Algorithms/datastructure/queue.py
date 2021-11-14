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

