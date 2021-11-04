import random


def binary_search(lst: iter, obj: int | str) -> int | None:
    lst_sorted = sorted(list(lst))
    low = 0
    high = len(lst_sorted)
    while low <= high:
        med = (low + high) // 2
        if lst_sorted[med] == obj:
            return med
        elif lst_sorted[med] > obj:
            high = med - 1
        else:
            low = med + 1
    return None


lst = (random.randint(1, 50) for _ in range(50))
# lst = sorted(list('fwelkjfqwoeivnawoqnqoiwerjvqweironvoqweirhvnqweivnedovniaavndvaddsvweiuvnwdsv'))
obj = random.randint(1, 50)
# obj = random.choice(lst)
print(binary_search(lst, obj))
