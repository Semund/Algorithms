def gcd_cycle(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int):
    return gcd_recursive(b, a % b) if b else a





