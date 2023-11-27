# вводим два числа
n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))

if m > n:
    step = 1
else:
    step = -1

sum = 0
count = 0

# находим сумму от n до m
for i in range(n, m + 1, step):
    sum += i
    count += 1
    
if n == m:
    count = 1

print("Сумма от n до m равна:", sum)
print("Среднее значение равно:", sum / count)