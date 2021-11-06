def quicksort(lst):
    def _quicksort(lst):
        if len(lst) < 2:
            return lst
        great = []
        equal = []
        less = []
        pivot = lst[len(lst) // 2]
        for elem in lst:
            if elem < pivot:
                less.append(elem)
            elif elem > pivot:
                great.append(elem)
            else:
                equal.append(elem)
        return _quicksort(less) + equal + _quicksort(great)

    return _quicksort(lst)

