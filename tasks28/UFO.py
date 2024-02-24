from typing import List

def Hexadecimal(n: int) -> int:

    l = list(str(n))
    sum_hex = 0
    for i in range(len(l)):
        sum_hex += int(l[i]) * (16 ** (len(l) - i - 1))

    return sum_hex

def Octal(n: int) -> int:

    l = list(str(n))
    sum_oct = 0
    for i in range(len(l)):
        sum_oct += int(l[i]) * (8 ** (len(l) - i - 1))

    return sum_oct

def UFO(N: int, data: List[int], octal: bool) -> List[int]:

    decimal_oct = []
    for i in range(N):
        decimal_oct.append(Octal(data[i]))

    decimal_hex = []
    for i in range(N):
        decimal_hex.append(Hexadecimal(data[i]))

    if octal:
        return decimal_oct
    
    return decimal_hex