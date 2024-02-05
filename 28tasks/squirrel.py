def squirrel(N: int) -> int:
    number = 1

    while N > 1:
        number *= N
        N -= 1

    while number >= 10:
        number //= 10

    return number