def LineAnalysis(line: str) -> bool:

    if line[0] != '*' or line[len(line) - 1] != '*':
        return False
    
    string_of_dots = line.replace('*', '')
    if string_of_dots == '':
        return True
        
    for i in range(len(string_of_dots)):
        if string_of_dots[i] != '.':
            return False
        
    if line.count('*') < 3:
        return True

    string_check = '*'
    for i in range(1, len(line)):
        if line[i] != '*':
            string_check += line[i]

        if line[i] == '*':
            break
    string_check *= len(line) // len(string_check) 
    string_check += '*'

    if string_check == line:
        return True
    return False