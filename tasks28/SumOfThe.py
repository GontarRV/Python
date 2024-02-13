from typing import List

def SumOfThe(N: int, data: List[int]) -> int:

    summary_amount = 0
    for i in range(len(data)):
        summary_amount += data[i]

    result = int(summary_amount / 2)

    return result