class Weapon:

    def __init__(self):
        self._damage = 0 # сила поражения, баллы
    
    def get_damage(self, dist): # дистанция до цели
        if dist < 0 or dist > 1:
            return 0
        return self._damage

class spear(Weapon):

    def __init__(self):
        self.__name = 'копье'
        self._damage = 10

class crossbow(Weapon):

    def __init__(self):
        self.__name = 'арбалет'
        self._damage = 15
        self.__range = 3

    def get_damage(self, dist):
        if dist > self.__range:
            return 0
        return (int)(self._damage)
        
class Pet:

    def __init__(self, Pet_hunger):
        self.__hunger = Pet_hunger  # голод значение от 0 до 100, %
        self._damage = 0    
    
    def get_damage(self, dist): # дистанция до цели
        if dist < 0 or dist > 1:
            return 0
        return self._damage
    
    def sound(self):
        print('Животное подает голос')

    def sleep(self):
        self.__health += 0.5
        self.__hunger -= 0.5

class raven(Pet):

    def __init__(self, Pet_hunger):
        super().__init__(Pet_hunger)
        self.__name = 'Ворон'
        self.__health = 20
        self._damage = 3

    def sound(self):
        print('Каааар кааар кар')
    
class wolf(Pet):

    def __init__(self, Pet_hunger):
        super().__init__(Pet_hunger)
        self.__name = 'Волк'
        self.__health = 40
        self._damage = 6

    def sound(self):
        print('Аууу аууу аууу')

class Survivor:

    def __init__(self, Survivor_name, Survivor_health,
                 Survivor_hunger, Survivor_energy, 
                 Survivor_workId, Survivor_speed):
        self.__name = Survivor_name  # имя выжившего
        self.__health = Survivor_health  # здоровье значение от 0 до 100, %
        self.__hunger = Survivor_hunger  # голод значение от 0 до 100, %
        self.__energy = Survivor_energy  # энергия значение от 0 до 100, %
        self.__speed = Survivor_speed  # скорость движения, км/ч
        self._hand = Weapon() # ячейка руки
        self._hand = Pet(100) # ячейка питомца
        self.__workId = Survivor_workId  # код текущей деятельности: 0 - отдыхает,
                                         # 1 - работает, 2 - сражается,
                                         # 3 - перемещается
    
    def Eat(self, food):
        self.__hunger += food
        if self.__hunger > 100:
            self.__hunger = 100
        self.__health += food / 10
        if self.__health > 100:
            self.__health = 100

    def Run(self, new_speed):
        self.__speed = new_speed
        self.__workId = 3

    
sur = Survivor('Rom', 50, 50, 50, 2, 0)
sur._hand = spear()
sur._pet = wolf(80)

print('Атака выжившего и питомца, составляет:', sur._hand.get_damage(1) + sur._pet.get_damage(1))

# Задание 4.2
import random
Kar = raven(80)
Fang = wolf(80)
pet = []

for i in range(500):
    if random.randint(1, 2) % 2 == 0:
        pet.append(Kar)
    else:
        pet.append(Fang)
    pet[i].sound()

