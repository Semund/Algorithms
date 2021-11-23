from timer import timer


@timer
def fast_pow_recursive(n: int, m: int):
    """Raise n-number to the power m-number using recursion"""
    def _fast_pow(n, m):
        if m == 1:
            return n
        return n * _fast_pow(n, m - 1) if m % 2 else _fast_pow(n ** 2, m // 2)
    return _fast_pow(n, m)


@timer
def fast_pow_cycle(n: int, m: int):
    """Raise n-number to the power m-number using cycle"""
    result = 1
    while m > 0:
        if m % 2:
            result *= n
            m -= 1
        n = n ** 2
        m //= 2
    return result


print(fast_pow_recursive(2, 400000000) == fast_pow_cycle(2, 400000000))
