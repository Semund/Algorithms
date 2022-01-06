from pprint import pprint


def levenshtein_distance(string_1: str, string_2: str) -> int:
    n = len(string_1)
    m = len(string_2)
    a = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        a[i][0] = i
    for j in range(1, m + 1):
        a[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            par_cost = 1 if string_1[i - 1] != string_2[j - 1] else 0
            a[i][j] = min(
                a[i - 1][j] + 1,  # delete
                a[i][j - 1] + 1,  # insert
                a[i - 1][j - 1] + par_cost  # replace
            )
    pprint(a)
    return a[n][m]


if __name__ == '__main__':
    s1 = "exponential"
    s2 = "polynomial"
    print(levenshtein_distance(s1, s2))
