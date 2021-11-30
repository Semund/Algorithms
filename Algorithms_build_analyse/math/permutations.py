def generate_permutations(n: int, m: int, prefix=None):
    """Generating all possible permutations of n-numbers in m-position with leading zeros"""
    if m == 0:
        print(*prefix, end=', ', sep='')
        return
    prefix = prefix or []
    for digit in range(n):
        if digit in prefix:
            continue
        prefix.append(digit)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


if __name__ == '__main__':

    generate_permutations(10, 6)