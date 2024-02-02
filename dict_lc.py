# from random import randint
# d = dict.fromkeys(("name", "tel"))
# dc = {i: randint(11111, 99999) for i in ("number", "tel")}
# d["name"] = "pasha"
# print(d, dc, dc["number"], sep="\n")
# print(d.get("a"))
# print(list(dc.items()))
# # 1
# """Создайте словарь person, в котором будут присутствовать
# ключи name, age, city.
# Выведите значение возраста из словаря person."""
#
# from faker import Faker
# fake = Faker()
# person = {
#         "name": fake.name(),
#         "age": 55,
#         "city": fake.city()
# }
# __import__('pprint').pprint(person)
# __import__('pprint').pprint(person["age"])

# # 2
# """Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из
# 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей."""
#
# car = {
#     "BMW": ["x1", "x2", "x3"],
#     "Tesla": ["s", "x", "y"],
# }
# print(car["BMW"][0], car["BMW"][-1], car["Tesla"][0], car["Tesla"][-1])
#
# 3
# """Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод True)
# d1 = {"a": 100. "b": 200. "c":300}
# d2 = {a: 300. b: 200, d:400}
#
# print(d1["b"] == d2["b"]"""
#
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
#
# print(d1["b"] == d2["b"])
#
# # 4
# """Дан словарь с числовыми значениями. Необходимо их
# все перемножить и вывести на экран."""
# from math import prod
#
# numbers = {i: i**2 for i in range(1, 8)}
#
# __import__("pprint").pprint(numbers.values())
# print(prod(numbers.values()))

# 5
# """Даны два списка одинаковой длины. Необходимо создать из них словарь
# таким образом, чтобы элементы первого списка были ключами, а элементы
# второго — соответственно значениями нашего словаря."""
#
# num = list(range(1, 7))
# let = list("abcdef")
#
# dc = dict(zip(num, let))
# print(dc)

# 6
# """Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей
# возьмите буквы строки, а значениями пусть будут числа, соответствующие
# количеству вхождений данной буквы в строку."""
#
# str = "pythonist"
#
# dc = {i: str.count(i) for i in str}
# print(dc)
#
# # dz
# """У вас есть словарь, где ключ – название продукта.
# Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров
# осталось в изначальном списке.
# """
# products = {"Apple": [1000, 5], "Samsung": [700, 10], "Asus": [800, 9]}
# for i in products:
#     print(f"{i} - {products[i][0]}$ - x{products[i][1]}")
# summa = 0
# while True:
#     prod = input("prod: ")
#     if prod == "no":
#         break
#     count = int(input("count: "))
#     if prod in products.keys() and products[prod][1] >= count:
#         products[prod][1] -= count
#         summa += products[prod][0] * count
#     else:
#         print("input error")
# print(f"summa {summa}$")
# for i in products:
#     print(f"{i} - {products[i][0]}$ - x{products[i][1]}")
#
"""
Дан словарь с данными. Написать программу авторизации, пользователь
вводит логин и пароль.
В случае, если не верный логин и (или) пароль - вывеси соответствующие
сообщение.
В случае авторизации - вывести приветствие по логину и роль.
Дать 5 попыток авторизации.

При желании - расширить функционал.
"""

auth_data = {
    "users": {
        "admin": {"password": "12345", "role": "ADMIN_ACCESS"},
        "мария": {"password": "12345", "role": "STUDENT_ACCESS"},
        "иван": {"password": "12345", "role": "STUDENT_ACCESS"},
        "гоша": {"password": "12345", "role": "STUDENT_ACCESS"},
    },
}

# login = input("login: ")
# pas = input("password: ")
# count = 0
#
# while count < 5:
#     for k, v in auth_data["users"].items():
#         if login == k and pas == v["password"]:
#             print(f'Hello {k} - {v["role"]}')
#             count += 5
#         else:
#             print("no_auth")
#             count += 1

count = 0

while count < 5:
    login = input("login: ")
    pas = input("password: ")

    if login in auth_data["users"].keys():
        if pas == auth_data["users"][login]["password"]:
            print(f'Hello {login} - {auth_data["users"][login]["role"]}')
            count += 5
    else:
        print("no auth")
        count += 1
