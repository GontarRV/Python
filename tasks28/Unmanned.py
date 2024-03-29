from typing import List

def Unmanned(L: int, N: int, track: List[int]) -> int:

    full_time = 0
    num = 0

    if L <= track[0][0]:
        return L
        
    for track_stop in track:
        full_time, num = time(full_time, num, track_stop)

    full_time = full_time + L - num
    
    return full_time

def time(full_time: int, num: int, track_stop: List[int]) -> int:
    
    full_time += track_stop[0] - num
    track_red_green = track_stop[1] + track_stop[2]
    num = track_stop[0]
        
    if full_time < track_stop[1]:
        full_time = track_stop[1]
        return full_time, num
        
    if track_red_green % full_time == 0:
        full_time += track_stop[1]
        return full_time, num
        
    if full_time % track_red_green >= track_stop[1]:
        return full_time, num
    full_time += track_stop[1] - (full_time % track_red_green)
    return full_time, num
