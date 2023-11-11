def bul(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        for j in range(len(s2)):
            if s2[j] != s1[i + j]:
                break
            elif j + 1 == len(s2):
                return True
    return False


s1 = '123123412'
s2 = '234'

print(bul(s1, s2))