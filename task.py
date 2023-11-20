class Survivor:

    def __init__(self, Survivor_name, Survivor_health,
                 Survivor_hunger, Survivor_thirst,
                 Survivor_energy, Survivor_workId, Survivor_speed):
        self.__name = Survivor_name  # имя выжившего
        self.__health = Survivor_health  # здоровье значение от 0 до 100, %
        self.__hunger = Survivor_hunger  # голод значение от 0 до 100, %
        self.__thirst = Survivor_thirst  # жажда значение от 0 до 100, %
        self.__energy = Survivor_energy  # энергия значение от 0 до 100, %
        self.__speed = Survivor_speed  # скорость движения, км/ч
        self.__workId = Survivor_workId  # код текущей деятельности: 0 - отдыхает,
                                         # 1 - работает, 2 - сражается,
                                         # 3 - перемещается
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_hunger(self):
        return self.__hunger
    
    def get_thirst(self):
        return self.__thirst
    
    def get_energy(self):
        return self.__energy
    
    def get_speed(self):
        return self.__speed


    def Eat(self, food):
        self.__hunger += food
        if self.__hunger > 100:
            self.__hunger = 100
        self.__health += food / 10
        if self.__health > 100:
            self.__health = 100

    def drink(self, liquid):
        self.__thirst += liquid
        if self.__thirst > 100:
            self.__thirst = 100
        self.__health += liquid / 10
        if self.__health > 100:
            self.__health = 100

    def Run(self, new_speed):
        self.__speed = new_speed
        self.__workId = 3


class Weapon:

    def __init__(self, knd, Weapon_name, Weapon_damage):
        self.__kind = knd # 0 - холодное оружие, 1 - дальнобойное оружие,
                        # 2 - взывчатка/граната
        if knd == 0:
            self.__name = Weapon_name # название
            self.__damage = Weapon_damage # сила поражения, баллы
            self.__range = 1 # дальность действия
        elif knd == 1:
            self.__name = Weapon_name 
            self.__damage = Weapon_damage
            self.__range = 3
        elif knd == 2:
            self.__name = Weapon_name 
            self.__damage = Weapon_damage
            self.__range = 3
    
    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_range(self):
        return self.__range

    def get_kind(self):
        return self.__kind        
        
    def get_damage(self, dist): # дистанция до цели
        if dist < 0:
            return 0
        
        if (self.__kind == 2 or self.__kind == 3) and dist > self.__range:
            return 0
        
        if self.__kind == 2 or self.__kind == 3:
            return self.__damage
        
        if dist > 1:
            return 0

class Pet:

    def __init__(self, Pet_name, Pet_kind, Pet_health, Pet_damage,
                 Pet_hunger, Pet_workId):
        self.__name = Pet_name  # имя питомца
        self.__kind = Pet_kind  # вид животного: 0 - ворон, 1 - писец, 2 - лиса
        self.__health = Pet_health  # здоровье значение от 0 до 100, %
        self.__damage = Pet_damage  # значение наносимого урона
        self.__hunger = Pet_hunger  # голод значение от 0 до 100, %
        self.__workId = Pet_workId  # код текущей деятельности: 0 - отдыхает,
        # 1 - работает, 2 - сражается,
        # 3 - перемещается, # 4 - спит

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_hunger(self):
        return self.__hunger
    
    def get_damage(self):
        return self.__damage
    
    def get_workId(self):
        return self.__workId
    
    def Eat(self, food):
        self.__hunger += food
        if self.__hunger > 100:
            self.__hunger = 100
        self.__health += food / 10
        if self.__health > 100:
            self.__health = 100

    def Heal(self, heal):
        self.__health += heal
        if self.__health > 100:
            self.__health = 100

    def sleep(self):
        self.__health += 0.5
        self.__hunger -= 0.5


my_survivor = Survivor('Роман', 70, 80, 80, 70, 0, 0)
my_survivor.drink(10)
print('Выживший', my_survivor.get_name(), 'выпил и повысил насыщение жидостью до',
      my_survivor.get_thirst(), 'и здоровье до', my_survivor.get_health())
my_survivor.Eat(10)
print('Выживший', my_survivor.get_name(), 'поел и повысил сытость до',
      my_survivor.get_hunger(), 'и здоровье до', my_survivor.get_health())
my_survivor.Run(5)
print("Скорость выжевшего", my_survivor.get_name(),
      'составляет:', my_survivor.get_speed(), 'км/ч')


my_pet = Pet('Каркуша', 0, 70, 10, 50, 0)
my_pet.Eat(10)
print('Питомец', my_pet.get_name(), 'ест и повышает сытость до',
      my_pet.get_hunger(), 'и здоровье до', my_pet.get_health())
my_pet.Heal(5)
print('Питомец', my_pet.get_name(), 'лечится и повышает здоровье до', my_pet.get_health())
my_pet.sleep()
print('Питомец', my_pet.get_name(), 'спит и повышает здоровье до',
      my_pet.get_health(), 'сытость падает до', my_pet.get_hunger())
