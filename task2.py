class domestic_animals: # 1-й родительский класс

    def __init__(self, w, a):
        self.weight = w
        self.age = a

    def feed(self, food):
        self.weight += food

    def cleen(self):
        pass


class goose(domestic_animals):

    def __init__(self, w, a):
        super().__init__(w, a)
        self.egg = 0

    def egg_laying(self):
        self.egg += 3

    def dead_goose(self):
        if self.age >= 1:
            self.poultry_meat = self.weight * 0.5
        else:
            print("Птица еще недостаточно выросла!")


class goat(domestic_animals):

    def __init__(self, w, a):
        super().__init__(w, a)
        self.milk = 0
        self.wool = 0

    def milking(self):
        self.milk += 5

    def shearing(self):
        self.wool += self.weight * 0.2


class house: # 2-й родительский класс

    def __init__(self):
        self.num_of_rooms = r
        self.num_of_doors = d

    def demolish(): # снос дома
        pass


class private_home(house):

    def __init__(self, n, t, r, d):
        super().__init__(r, d)
        self.garden = n  # количество соток
        self.apple_trees = t  # количество яблонь

    def make_an_extension(self):
        self.num_of_rooms += 1

    def plant_apple(self):
        self.apple_trees += 1


class Multi_storey_building(house):

    def __init__(self, f, r, d):
        super().__init__(r, d)
        self.flat = f

    def choose_a_company(self): # выбор управляющей компании
        pass

    def organize_a_meeting(self): # организация собрания жильцов
        pass
