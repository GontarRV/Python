from typing import List

def MisterRobot(N: int, data: List[int]) -> bool:

    if data == sorted(data):
        return True

    for i in range(N):
        for j in range(N - 2):
            if data[j:j + 3] != sorted(data[j:j + 3]):
                data[j:j + 3] = rotation(data[j:j + 3])
            if data == sorted(data):
                return True
    return False
            

def rotation(data_three: List[int]) -> List[int]:

    for i in range(3):
        data_three = [data_three[1], data_three[2], data_three[0]]
        if data_three == sorted(data_three):
            break
    return data_three