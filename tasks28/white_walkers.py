def white_walkers(village: str) -> bool:

    l = list(village)

    flag = False
    digit = 0

    for i in range(len(l)):
        if l[i].isdigit():
            flag = walker(l, i, flag)

    return flag

def walker(l , i, flag):

    sum = 0
    counter = 0

    for j in range(i, len(l)):

        if l[j].isdigit() and sum == 0:
            num1 = l[j]
            sum += int(l[j])

        if l[j] == '=':
            counter += 1

        if l[j].isdigit() and l[j] != num1:
            sum += int(l[j])

            if sum != 10:
                break

        if sum == 10 and counter != 3:
            flag = False
            break

        if sum == 10 and counter == 3:
            flag = True
            break

    return flag