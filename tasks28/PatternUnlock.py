from typing import List

def PatternUnlock(N: int, hets: List[int]) -> str:
    
    c = 2 ** 0.5
    distance_between_points = {'61': 1, '62': c, '65': 1, '56': 1,
                               '51': c, '52': 1, '53': c, '54': 1,
                               '45': 1, '42': c, '43': 1, '16': 1,
                               '15': c, '12': 1, '18': c, '19': 1,
                               '26': c, '21': 1, '29': c, '28': 1,
                               '27': c, '23': 1, '24': c, '25': 1,
                               '34': 1, '35': c, '32': 1, '38': c,
                               '37': 1, '91': 1, '92': c, '98': 1,
                               '89': 1, '81': c, '82': 1, '83': c,
                               '87': 1, '73': 1, '72': c, '78': 1}

    sum = 0
    hets = list(hets)
    for i in range(N - 1):
        if str(hets[i]) + str(hets[i + 1]) in distance_between_points:
            sum += distance_between_points[str(hets[i]) + str(hets[i + 1])]

    sum = str(round(sum * 10 ** 5))

    access_code = ''
    for i in range(len(sum)):
        if sum[i] != '0':
            access_code += sum[i]

    return access_code