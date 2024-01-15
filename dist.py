import random

#задание 1
mydict = {}
for i in range(100):
    mydict['key' + str(i)] = random.randint(1,10000)

for i in range(100):    
    print(mydict.get('key' + str(i)))
mydict.clear()

#задание 2
def repeats(list, N):
    repeats_elem = {}

    for item in list:
        if item in repeats_elem:
            repeats_elem[item] += 1
        else:
            repeats_elem[item] = 1
    
    for key, value in repeats_elem.items():
        if value >= N:
            print(key)

list = []

for i in range(100):
    list.append(random.randint(1, 10))

repeats(list, 10)
