def printing_even_indexes(array: list):
    if len(array) <= 1:
        return

    print(array[0])
    del array[:2]

    printing_even_indexes(array)