from typing import List

def BiggerGreater(input: str) -> str:
    l = list(input)
    for i in range(len(l) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                return ''.join(transposition(j + 1, l))
    return ""

def transposition(n: int, l: list) -> List[str]:
    for i in range(n, len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]
    return l