def printing_only_even_values(array: list, move: int = 0):
    if len(array) <= move:
        return
    
    if array[move] % 2 == 0:
        print(array[move])

    printing_only_even_values(array, move + 1)
    
