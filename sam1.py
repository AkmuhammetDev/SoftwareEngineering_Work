# Класс Tomato
class Tomato:
    # Статическое свойство states со стадиями созревания
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    # Метод __init__ с динамическими свойствами _index и _state
    def __init__(self, index):
        self._index = index  # динамическое приватное свойство
        self._state = 0      # динамическое приватное свойство, начальная стадия

    # Метод для перехода на следующую стадию
    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Помидор {self._index} теперь на стадии: {Tomato.states[self._state]}')

    # Проверка, созрел ли помидор
    def is_ripe(self):
        return self._state == 3


# Класс TomatoBush
class TomatoBush:
    # Метод __init__ создает список помидоров
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]  # динамическое свойство

    # Перевод всех помидоров на следующую стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверка, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Очистка списка после сбора урожая
    def give_away_all(self):
        self.tomatoes = []


# Класс Gardener
class Gardener:
    # Метод __init__ с динамическими свойствами name и _plant
    def __init__(self, name, plant):
        self.name = name          # публичное свойство
        self._plant = plant       # приватное свойство

    # Садовник работает — растение растет
    def work(self):
        print(f'{self.name} ухаживает за растением...')
        self._plant.grow_all()

    # Сбор урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Еще не все помидоры созрели!')

    # Статический метод — справка
    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Садовник ухаживает за кустом томатов.')
        print('2. Томаты проходят стадии: отсутствует, цветение, зеленый, красный.')
        print('3. Собирать урожай можно, когда все томаты красные.\n')


# Тесты
if __name__ == '__main__':
    # 1) Вызов справки
    Gardener.knowledge_base()

    # 2) Создание объектов
    bush = TomatoBush(3)
    gardener = Gardener('Вася', bush)

    # 3) Ухаживаем за кустом
    gardener.work()
    gardener.work()

    # 4) Пытаемся собрать урожай (еще не все созрели)
    gardener.harvest()

    # 5) Еще раз ухаживаем и собираем урожай
    gardener.work()
    gardener.harvest()