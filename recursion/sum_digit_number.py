def sum_digit_number(N: int) -> int:
    if len(str(N)) == 1:
        return N
    return int(str(N)[0]) + sum_digit_number(int(str(N)[1:]))