from typing import List

def MaximumDiscount(N: int, price: List[int]) -> int:

    if N < 3:
        sum_price = 0

    sum_price = 0
    while N > 2:
        three_item, price = maximumprice(price)
        sum_price += min(three_item)
        N -= 3

    return sum_price


def maximumprice(price: List[int]):
    
    three_item =  []
    for i in range(3):
        three_item.append(max(price))
        price.remove(max(price))
    return three_item, price