def find_two_max(max_one: int, max_two: int, array: list) -> int:

    if array == []:
        return max_two

    if array[0] >= max_one:
        max_one, max_two = array[0], max_one
    elif array[0] > max_two:
        max_second = array[0]

    array.pop(0)
    
    return find_two_max(max_one, max_two, array) 

def find_second_max_num(array: list) -> int:

    max_first, max_second = array[0], array[1]
    if max_first < max_second:
        max_first, max_second = array[1], array[0]

    array = array[2:]

    return find_two_max(max_first, max_second, array)