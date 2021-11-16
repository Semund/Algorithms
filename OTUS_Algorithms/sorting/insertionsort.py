from random import randint
from timer import timer

@timer
def insertion_sort(list_for_sort: list):
    lst = list_for_sort[:]
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = item_to_insert
    return lst

if __name__ == '__main__':
    list_for_sort = [randint(1, 1000000) for _ in range(10000)]
    # list_for_sort = list(range(100000))
    print(insertion_sort(list_for_sort))
