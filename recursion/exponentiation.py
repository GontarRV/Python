def exponentiation(N: int, M: int) -> int:
    # предполагаем, что число M > 1
    if M == 0:
        return 1
    return N * exponentiation(N, M - 1)