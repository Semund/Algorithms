def find_prefix(string):
    n = len(string)
    prefix_list = [0] * n
    i, j = 1, 0
    while i < n:
        if string[i] == string[j]:
            prefix_list[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                prefix_list[i] = 0
                i += 1
            else:
                j = prefix_list[j - 1]
    return prefix_list


def kmp_matcher(string, substring):
    prefix_list = find_prefix(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while i < n:
        if string[i] == substring[j]:
            i += 1
            j += 1
            if j == m:
                print("Подстрока найдена. Индекс строки: ", i - m)
                break
        else:
            if j > 0:
                j = prefix_list[j - 1]
            else:
                i += 1
    if i == n:
        print("Подстрока не найдена")


