from typing import List

def odometer(oksana: List[int]) -> int:
    timepoint = 0
    distance = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            speed = oksana[i]
        else:
            time = oksana[i] - timepoint
            timepoint = oksana[i]
            distance += time * speed

    return distance