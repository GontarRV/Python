class Cat:
    def __init__(self, name, weight, freq):
        self.name = name
        self.weight = weight
        self.freq = freq

cats = []

with open('cats.txt') as f:
    cat_info = f.readline().rstrip()

    while cat_info != '':
        cat_parameters = cat_info.split()
        cat_info = f.readline().rstrip()
        name = cat_parameters[0]

        try:
            weight = float(cat_parameters[1])
            freq = float(cat_parameters[2])
        except:
            continue

        cats.append(Cat(name, weight, freq))

print(cats)