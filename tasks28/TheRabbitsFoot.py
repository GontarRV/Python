import math

def TheRabbitsFoot(s: str, encode: bool) -> str:

    if encode:
        s_without_spaces = s.replace(' ', '')
        M = math.ceil(len(s) ** 0.5)
        if (M - 1) * M >= len(s):
            N = M - 1
        else:
            N = M
        
        matrix = []
        while s_without_spaces != '':
            s1 = s_without_spaces[0:M]
            matrix.append(s1)
            s_without_spaces = s_without_spaces[M:]


        k = 0
        t_matrix = []
        code = ""
        for i in range(N):
            for j in matrix:
                if k == len(j):
                    del matrix[matrix.index(j)]
                    continue
                code += j[i]
            k += 1
            t_matrix.append(code)
            code = ""

        good_code = ''
        for k in t_matrix:
            good_code += k
            good_code += ' '
        good_code = good_code.rstrip()

    else:
        k = 0
        l = s.split()
        good_code = ''
        for i in range(len(l[0])):
            for j in l:
                if len(j) < k + 1:
                    continue
                good_code += j[k]
            k += 1

    return good_code

