from math import ceil, log2


class MaxHeap:
    def __init__(self, *elem):
        self.heap = list(elem)
        self.size = len(self.heap)
        self.heapify()

    def heapify(self):
        for index in range(self.size // 2, -1, -1):
            self.sift_down(index)

    def sift_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.sift_down(largest)

    def sift_up(self, index):
        while index > 0 and self.heap[index] > self.heap[(index - 1) // 2]:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2

    def insert(self, elem):
        self.heap.append(elem)
        self.size += 1
        self.sift_up(-1)

    def extract_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_element = self.heap.pop()
        self.size -= 1
        self.sift_down(0)
        return max_element

    def remove(self, index):
        self.heap[index] = self.heap[0] + 1
        self.sift_up(index)
        self.extract_max()

    def get_max(self):
        return self.heap[0]

    def change_priority(self, index, priority):
        old_priority = self.heap[index]
        self.heap[index] += priority
        if old_priority < self.heap[index]:
            self.sift_up(index)
        elif old_priority > self.heap[index]:
            self.sift_down(index)

    def print_heap(self):
        heap_hight = ceil(log2(self.size))
        while self.size < 2 ** heap_hight:
            self.heap.append('-')
            self.size += 1
        for i in range(heap_hight):
            current_heap_level = self.heap[2 ** i - 1: 2 ** (i + 1) - 1]
            print_line = f'{" " * 2 ** (heap_hight - i - 1)}'
            for elem in current_heap_level:
                sep_spaces = 2 ** (heap_hight - i)
                print_line += f'{elem:<{sep_spaces}}'
            print(print_line)

hp = MaxHeap(*range(128))
hp.print_heap()
