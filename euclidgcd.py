def GCD_recursive(num1: int, num2: int) -> int:
    """Function for finding GCD using a recursion"""
    return GCD_recursive(num2, num1 % num2) if num2 else num1


def GCD_loop(num1: int, num2: int) -> int:
    """Function for finding GCD using a loop"""
    while num2:
        num1, num2 = num2, num1 % num2
    return max(num1, num2)

