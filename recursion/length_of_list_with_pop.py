def length_of_list_with_pop(array: list) -> int:
    if array == []:
        return 0
    array.pop(0)
    return 1 + length_of_list_with_pop(array)