from random import randint
from timer import timer


@timer
def bubble_sort(list_for_sort):
    lst = list_for_sort[:]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
    return lst


if __name__ == '__main__':
    # list_for_sort = [randint(1, 100000) for _ in range(20000)]
    list_for_sort = list(range(100000))
    print(bubble_sort(list_for_sort) == sorted(list_for_sort))
