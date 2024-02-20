def BigMinus(s1: str, s2: str) -> str:
    
    if s1 == s2:
        return '0'
        
    for i in range(len(s1)):
        if len(s1) != len(s2):
            break
        else:
            if s1[i] == s2[i]:
                continue
            elif s1[i] > s2[i]:
                s_min = s2
                s_max = s1
                break
            else:
                s_min = s1
                s_max = s2
                break

    if len(s1) > len(s2):
        s_min = s2
        s_max = s1
    elif len(s1) < len(s2):
        s_min = s1
        s_max = s2

    loan = 0
    margin = []
    for i in range(len(s_min)):
        if int(s_max[len(s_max) - i - 1]) - loan >= int(s_min[len(s_min) - i - 1]):
            residual = int(s_max[len(s_max) - i - 1]) - loan - int(s_min[len(s_min) - i - 1])
            margin.insert(0, str(residual))
            loan = 0
        else:
            residual = 10 + int(s_max[len(s_max) - i - 1]) - loan - int(s_min[len(s_min) - i - 1])
            loan = 1
            margin.insert(0, str(residual))
    
    s = s_max[:(len(s_max) -len(s_min))]
    
    for i in range(len(s)):
        if loan == 1 and s[len(s) - i - 1] != '0':
            s_loan = int(s[len(s) - i - 1]) - 1
            s = s[:(len(s) - i - 1)] + str(s_loan)
            break
        if loan == 1 and s[len(s) - i - 1] == '0':
            residual = 10 + int(s[len(s) - i - 1]) - 1
            margin.insert(0, str(residual))
        
    for num in margin:
            s += str(num)
    
    s = int(s)
    return str(s)