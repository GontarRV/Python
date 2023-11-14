class Riflemen:
    rank = 1
    cp = 50  # боевая мощь
    wpn_atk = 36  # атака оружием
    tac_atk = 60  # тактическая атака
    wpn_def = 17  # защита оружия
    tac_def = 17  # тактическая защита
    hp = 61  # очки здоровья
    speed = 11  # скорость
    load = 0.4  # загрузка ресурсами


class Hero:
    level = 1
    fraction = 'Watchers'  # фракция наблюдателей
    specialization = Riflemen()  # стрелки
    army = 100  # количество юнитов в армии
    strength = 147  # сила
    intellect = 203  # интеллект
    agility = 161  # ловкость
    vitality = 54  # живучесть(телосложение)
    luck = 110  # удача


hero1 = Hero()
hero2 = hero1  # hero1 и hero2 обращаются к одной ячейке памати
hero3 = Hero()

riflemen1 = Riflemen()
riflemen2 = riflemen1  # riflemen1 и riflemen2 обращаются к одной ячейке памяти
riflemen3 = Riflemen()
