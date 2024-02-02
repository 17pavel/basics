# 1. Написать функцию которая принимает 2 параметра: число часов и число минут и выводит число секунд на экран
import random


def get_seconds(hours, minutes):
    seconds = int(minutes) * 60 + int(hours) * 3600
    print(seconds)


# 2. Написать функцию которая принимает 2 параметра и возвращает список чисел от первого до второго
def get_range(from_number, to_number):
    numbers = []
    numbers += [i for i in range(from_number, to_number + 1)]
    return numbers


# 3. Написать функцию которая принимает список чисел и возвращает наибольшее из чисел, встроенные
# функции использовать нельзя
def get_max(numbers):
    max_number = -9999999999999999999
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number


if __name__ == '__main__':
    get_seconds(2, 22)

    print(get_range(-7, 17))
    lst = [random.randint(-99999, 999999) for i in range(5)]
    print(lst, get_max(lst))

# 4
"""Простейший калькулятор c введёнными двумя числами вещественного типа. 
Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.  
Обработать ошибку: “Деление на ноль” 
Ноль использовать в качестве завершения программы (сделать как отдельную операцию). """


def add_numbers(a, b):
    return a + b


def sub_numbers(a, b):
    return a - b


def mult_numbers(a, b):
    return a * b


def div_numbers(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = 0

    return res


while True:

    oper = input("oper: ")
    if oper == "0":
        break
    x = int(input("a: "))
    y = int(input("b: "))

    if oper == "+":
        print(add_numbers(x, y))
    if oper == "-":
        print(sub_numbers(x, y))
    if oper == "*":
        print(mult_numbers(x, y))
    if oper == "/":
        print(div_numbers(x, y))
