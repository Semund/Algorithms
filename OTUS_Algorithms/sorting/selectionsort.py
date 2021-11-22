from random import randint
from timer import timer


@timer
def selection_sort(list_for_sort):
    lst = list_for_sort[:]
    for i in range(len(lst) - 1):
        min_item_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_item_index]:
                min_item_index = j
        lst[i], lst[min_item_index] = lst[min_item_index], lst[i]
    return lst


if __name__ == '__main__':
    list_for_sort = [randint(1, 1000000) for _ in range(10000)]
    # list_for_sort = list(range(10000))
    print(selection_sort(list_for_sort) == sorted(list_for_sort))

