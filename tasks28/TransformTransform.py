from typing import List

def TransformTransform(A: List[int], N: int) -> bool:
    
    BB = Transform(Transform(A))
    sum_transform = sum(BB)

    if sum_transform % 2 == 0:
        return True
    return False

def Transform(A: List[int]) -> List[int]:
    
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            max_num = max(A[j:k + 1])
            B.append(max_num)
    return B