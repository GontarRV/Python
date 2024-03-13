def SherlockValidString(s: str) -> bool:
    
    glos = {}
    for el in s:
        glos[el] = s.count(el)
        
    glos_values = glos.values()
    glos_values = sorted(glos_values)
    if glos_values[-1] - glos_values[0] > 1:
        return False

    if glos_values[-1] > glos_values[-2] or len(glos_values) == 1:
        return True

    if glos_values[-1] == glos_values[0] or (glos_values[0] == 1 and glos_values[1] == 2):
        return True

    return False