def sum_digit_number(N: int) -> int:
    if (N // 10) < 1:
        return N
    return (N % 10) + sum_digit_number(N // 10)

