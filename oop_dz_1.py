"""1
Напишите программу с классом Car.
Создайте динамические свойства класса Car — color (цвет), type (тип), year (год). Напишите пять методов.
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
Третий — присвоение автомобилю года выпуска.
Четвертый метод — присвоение автомобилю типа.
Пятый — присвоение автомобилю цвета"""


class Car:

    def __init__(self, color, type_, year):
        self.color = color
        self.type_ = type_
        self.year = year

    @staticmethod
    def start():
        print("Автомобиль заведен")

    @staticmethod
    def stop():
        print("Автомобиль заглушен")

    def year_(self, year: int):
        self.year = year
        print(vars(self))

    def type__(self, type_: str):
        self.type_ = type_
        print(vars(self))

    def color_(self, color: str):
        self.color = color
        print(vars(self))


car = Car("black", "van", 2000)
car.start()
car.stop()
car.year_(2020)
car.type__("bus")
car.color_("red")

"""2
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
 (отвечающий за добавку к выбираемому лимонаду, тип данных строка). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
 а иначе отобразится следующая фраза: «Обычная газировка»."""


class Soda:

    def __init__(self, ingredient=None):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient is None:
            print("Обычная газировка")
        else:
            print(f"Газировка и {self.ingredient}")


s = Soda()
s_2 = Soda("лимон")
s.show_my_drink()
s_2.show_my_drink()

"""3
Создайте класс Example. В нём пропишите 3 метода. Две переменные задайте статически(int), две динамически(int).
Первый метод: создайте переменную внутри этой функции и выведите её.
Второй метод: верните сумму 2-ух статичных переменных.
Третий метод: верните результат возведения первой динамической переменной во вторую динамическую переменную.

Создайте объект класса.
Вызовите эти методы.
Напечатайте первое статическое свойство."""


class Example:
    a = 7
    b = 77

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def create(self):
        self.e = 777
        print(self.e)

    @classmethod
    def sum_(cls):
        print(cls.a + cls.b)

    def pow_(self):
        print(self.c**self.d)


ex = Example(3, 33)
ex.create()
ex.sum_()
ex.pow_()
print(ex.a)

"""4
Калькулятор.
Создайте класс, где реализованы функции(методы) математических операций. А также функция, для ввод данных. """


class Calc:

    def add(self, a, b):
        print(a + b)

    def sub(self, a, b):
        print(a - b)

    def mult(self, a, b):
        print(a * b)

    def div(self, a, b):
        # if b != 0:
        #     print(a / b)
        # else:
        #     raise ZeroDivisionError("деление на ноль!!!")
        try:
            print(a / b)
        except ZeroDivisionError:
            print("деление на ноль!!!")


calc = Calc()
calc.div(3, 0)
calc.div(3, 5)

"""dz
Два метода в классе, один принимает в себя либо строку, либо число.
Если я передаю строку, то смотрим: 
если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные; 
если число то, произведение суммы чётных цифр на длину числа. 
Длину строки и числа искать во втором методе."""


class Dz:

    def run(self):
        self.s = input(": ")
        if self.s.isdigit():
            summa = 0
            for i in self.s:
                if int(i) % 2 == 0:
                    summa += int(i)
            print(summa * self.len_())
        else:
            count_g = 0
            count_s = 0
            ls = []
            lg = []
            for i in self.s:
                if i in "eyuioa":
                    count_g += 1
                    lg.append(i)
                else:
                    count_s += 1
                    ls.append(i)
            print(lg if count_s * count_g <= self.len_() else ls)

    def len_(self):
        return len(self.s)


dz = Dz()
dz.run()
