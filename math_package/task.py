from math_1.area import area
from volume import volume



l1 = int(input("Введите длину помещения:"))
l2 = int(input("Введите ширину помещения:"))
h = int(input("Введите высоту помещения:"))


# вычисляем площадь помещения
print("Площадь помещения равна:", area(l1, l2) )

# вычисляем объем помещения
print("Объем помещения равен:", volume(l1, l2, h))