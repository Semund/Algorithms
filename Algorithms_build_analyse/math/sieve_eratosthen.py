def sieve_of_eratosthenes(n: int):
    lst = [False, False] + [True for _ in range(2, n + 1)]
    i = 2
    while i ** 2 < n:
        if lst[i]:
            for j in range(i ** 2, n + 1, i):
                lst[j] = False
        i += 1
    return [i for i in range(n + 1) if lst[i]]
