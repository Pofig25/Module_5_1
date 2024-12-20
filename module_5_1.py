class House:                                            # Создайте класс House.
    def __init__(self, name, number_of_floors):         # Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
        self.name = name                                # Внутри метода __init__ создайте атрибуты объекта self.name
        self.number_of_floors =  number_of_floors       # и self.number_of_floors, присвойте им переданные значения.

    def go_to(self, new_floor):                         # Создайте метод go_to с параметром new_floor
        for i in range(1, new_floor + 1):               # и напишите логику внутри него на основе описания задачи
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break
                                                        # Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Горский', 18)                            # h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)                        # h2 = House('Домик в деревне', 2)
h1.go_to(5)                                             # h1.go_to(5)
h2.go_to(10)                                            # h2.go_to(10)
