from typing import List

def WordSearch(lenght: int, s: str, subs: str) -> List[int]:
    
    slist = []
    slist = s.split()

    s1 = ''
    s1list = [] 
    for i in range(len(slist)):
        word = slist[i]

        if len(word) <= lenght:
            if len(s1 + word) <= lenght:
                s1 += word + ' '
            elif len(s1 + word) > lenght:
                s1list.append(s1.strip())
                s1 = word + ' '

        if len(word) > lenght:
            if s1 != '':
                s1list.append(s1.strip())

            while len(word) > lenght:
                s11 = word[:lenght]
                word = word[lenght:]
                s1list.append(s11)
                s1 = word + ' '

    if s1 != '':
        s1list.append(s1.strip())

    return_list = []
    for i in range(len(s1list)):
        if subs in s1list[i]:
            return_list.append(1)
        else:
            return_list.append(0)

    return return_list 