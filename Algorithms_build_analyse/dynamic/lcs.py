def restore_lcs(s1, s2, table):
    lcs = []
    i = len(s1)
    j = len(s2)
    while table[i][j] != 0:
        if table[i][j] == table[i][j - 1]:
            j -= 1
        elif table[i][j] == table[i - 1][j]:
            i -= 1
        else:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
    return lcs[::-1]


def find_lcs(s1: str, s2: str):
    """
    Finding a longest common subsequence
    """
    n = len(s1)
    m = len(s2)
    c = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    lcs = restore_lcs(s1, s2, c)
    return lcs


if __name__ == '__main__':

    s1 = "accggtcgagtgcgcggaagccggccgaa"
    s2 = "gtcgttcggaatgccgttgctctgtaaa"
    print(find_lcs(s1, s2))

