def printing_only_even_values(array: list):
    if array == []:
        return
    
    if array[0] % 2 == 0:
        print(array[0])
    array.pop(0)

    printing_only_even_values(array)