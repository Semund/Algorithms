import random
from timer import timer


@timer
def selection_sort(lst: list) -> list:
    sorting_lst = lst[:]
    n = len(sorting_lst)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if sorting_lst[j] < sorting_lst[min_ind]:
                min_ind = j
        sorting_lst[i], sorting_lst[min_ind] = sorting_lst[min_ind], sorting_lst[i]
    return sorting_lst


no_sorted_list = [random.randint(1, 1000) for _ in range(2000)]
my_sorted_list = selection_sort(no_sorted_list)
print(sorted(no_sorted_list) == my_sorted_list)