class Survivor:

    def __init__(self, Survivor_name, Survivor_health,
                 Survivor_hunger, Survivor_thirst,
                 Survivor_energy, Survivor_workId, Survivor_speed):
        self.name = Survivor_name  # имя выжившего
        self.health = Survivor_health  # здоровье значение от 0 до 100, %
        self.hunger = Survivor_hunger  # голод значение от 0 до 100, %
        self.thirst = Survivor_thirst  # жажда значение от 0 до 100, %
        self.energy = Survivor_energy  # энергия значение от 0 до 100, %
        self.speed = Survivor_speed  # скорость движения, км/ч
        self.workId = Survivor_workId  # код текущей деятельности: 0 - отдыхает,
        # 1 - работает, 2 - сражается,
        # 3 - перемещается

    def Eat(self, food):
        self.hunger += food
        if self.hunger > 100:
            self.hunger = 100
        self.health += food / 10
        if self.health > 100:
            self.health = 100

    def drink(self, liquid):
        self.thirst += liquid
        if self.thirst > 100:
            self.thirst = 100
        self.health += liquid / 10
        if self.health > 100:
            self.health = 100

    def Run(self, new_speed):
        self.speed = new_speed
        self.workId = 3


class Pet:

    def __init__(self, Pet_name, Pet_kind, Pet_health, Pet_damage,
                 Pet_hunger, Pet_workId):
        self.name = Pet_name  # имя питомца
        self.kind = Pet_kind  # вид животного: 0 - ворон, 1 - писец, 2 - лиса
        self.health = Pet_health  # здоровье значение от 0 до 100, %
        self.damage = Pet_damage  # значение наносимого урона
        self.hunger = Pet_hunger  # голод значение от 0 до 100, %
        self.workId = Pet_workId  # код текущей деятельности: 0 - отдыхает,
        # 1 - работает, 2 - сражается,
        # 3 - перемещается, # 4 - спит

    def Eat(self, food):
        self.hunger += food
        if self.hunger > 100:
            self.hunger = 100
        self.health += food / 10
        if self.health > 100:
            self.health = 100

    def Heal(self, heal):
        self.health += heal
        if self.health > 100:
            self.health = 100

    def sleep(self):
        self.health += 0.5
        self.hunger -= 0.5


my_survivor = Survivor('Роман', 70, 80, 80, 70, 0, 0)
my_survivor.drink(10)
print('Выживший', my_survivor.name, 'выпил и повысил насыщение жидостью до',
      my_survivor.thirst, 'и здоровье до', my_survivor.health)
my_survivor.Eat(10)
print('Выживший', my_survivor.name, 'поел и повысил сытость до',
      my_survivor.hunger, 'и здоровье до', my_survivor.health)
my_survivor.Run(5)
print("Скорость выжевшего", my_survivor.name,
      'составляет:', my_survivor.speed, 'км/ч')


my_pet = Pet('Каркуша', 0, 70, 10, 50, 0)
my_pet.Eat(10)
print('Питомец', my_pet.name, 'ест и повышает сытость до',
      my_pet.hunger, 'и здоровье до', my_pet.health)
my_pet.Heal(5)
print('Питомец', my_pet.name, 'лечится и повышает здоровье до', my_pet.health)
my_pet.sleep()
print('Питомец', my_pet.name, 'спит и повышает здоровье до',
      my_pet.health, 'сытость падает до', my_pet.hunger)
