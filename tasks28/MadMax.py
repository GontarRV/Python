from typing import List
import random

def MadMax(N: int, Tele: List[int]) -> int:

    if N != 1:
        for i in range(N):
            for j in range(N):
                if Tele[i] < Tele[j]:
                    Tele[i], Tele[j] = Tele[j], Tele[i]

        for i in range(N // 2, N):
            for j in range(N // 2, N):
                if Tele[i] > Tele[j]:
                    Tele[i], Tele[j] = Tele[j], Tele[i]

    return Tele