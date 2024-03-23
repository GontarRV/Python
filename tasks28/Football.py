from typing import List

def Football(F: List[int], N: int) -> bool:

    for i in range(N - 1):
        for j in range(i + 1, N):
            F[i], F[j] = F[j], F[i]
            if F == sorted(F):
                return True
            F[i], F[j] = F[j], F[i]
    
    num1 = None
    num2 = None
    for i in range(N - 1):
        if F[i] > F[i + 1]:
            num1 = i
            break
        
    for i in range(N - 1, 0, -1):
        if F[i] < F[i - 1]:
            num2 = i
            break
            
    L = F[:num1] + F[num1:num2 + 1][::-1] + F[num2 + 1:]
    if L == sorted(F):
        return True
    return False