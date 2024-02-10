from typing import List

def SynchronizingTables(N: int, ids: List[int],
                        salary: List[int]) -> List[int]:
    
    ordered_array = []
    ordered_array.extend(ids)
    ordered_array.sort()

    salary.sort()

    dist = {}
    for i in range(N):
        dist[ordered_array[i]] = salary[i]

    truesalary = []
    for i in range(N):
        truesalary.append(dist.get(ids[i]))

    return truesalary
