# 1
from random import randint
#
#
# def uniq(lst_):
#     res = []
#     for el in lst_:
#         if lst_.count(el) == 1:
#             res.append(el)
#     print(res)
#
#
# ls = [
#     "p",
#     3,
#     4,
#     5,
#     6,
#     7,
#     "p",
#     5,
#     4,
#     3,
# ]
#
# uniq(ls)
#
# # 2
#
#
# def pairs(lst_):
#     not_pairs = []
#     pairs = []
#     for el in lst_:
#         if el not in not_pairs:
#             not_pairs.append(el)
#         else:
#             pairs.append(el)
#
#     print(pairs, len(pairs))
#
#
# pairs(ls)
#
# # 3
#
# C1 = tuple(randint(1, 999) for i in range(9))
# C2 = tuple(randint(1, 999) for i in range(9))
#
# print(C1, C2, sep="\n")
#
# if sum(C1) > sum(C2):
#     print(f"sum C1 {sum(C1)}")
# else:
#     print(f"sum C2 {sum(C2)}")
#
#
# def pozition(func):
#     def wrapper(lst_):
#         a = func(lst_)
#         return a, lst_.index(a) + 1
#
#     return wrapper
#
#
# print(pozition(min)(C1), pozition(max)(C1))
# print(pozition(min)(C2), pozition(max)(C2))
#
# # 4
# str_ = "An apple a day keeps the doctor away"
#
# dict_ = {}
# for i in str_:
#     dict_.update({i: str_.count(i)})
# print(dict_)
#
#
# # 5
#
# shop = {
#     "торт": [["мука, сахар, вода, крем"], 2, 10],
#     "сок": [["сахар, вода"], 1, 25],
#     "кекс": [["мука, сахар, вода"], 1.8, 30],
#     "вода": [["вода"], 0.5, 20],
# }
# menu = {
#     1: "посмотреть описание",
#     2: "посмотреть цену",
#     3: "посмотреть количество",
#     4: "посмотреть всю информацию",
#     5: "купить",
#     0: "до свидания",
# }
#
#
# print("сегодня в продаже", *shop.keys())
#
#
# def choise():
#     while True:
#         print(menu)
#         mn = int(input("сделайте выбор: "))
#         if mn == 0:
#             print("до свидания")
#             break
#         ch = input("выберите продукт: ")
#         if mn == 1:
#             print(ch, shop[ch][0])
#         elif mn == 2:
#             print(ch, shop[ch][1])
#         elif mn == 3:
#             print(ch, shop[ch][2])
#         elif mn == 4:
#             print(ch, shop[ch])
#         elif mn == 5:
#             buy(ch)
#
#
# def buy(prod):
#     buy_ = {}
#     cost = 0
#     while True:
#         count = int(input("сколько?: "))
#         buy_.update({prod: count})
#         shop[prod][2] -= count
#         cost += shop[prod][1] * count
#         prod = input("что-то еще?: ")
#         if prod == "нет":
#             break
#
#     print(f"ваша покупка: {buy_} с вас {cost} рублей")
#     __import__("pprint").pprint(shop)
#
#
# choise()
#
# # 6
#
# lst_1 = [randint(1, 37) for i in range(15)]
# lst_2 = [randint(1, 37) for i in range(15)]
# set_1 = set(lst_1)
# set_2 = set(lst_2)
# print(lst_2, lst_1)
# res = set_1 & set_2
# print(res, len(res))
#
# # 7
#
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
#
# try:
#     print(num1 / num2)
# except ZeroDivisionError:
#     print(0)
# else:
#     print((num1 / num2) ** 2)
# finally:
#     print("good bay")
#
# 8

with open("example.txt", "r") as f:
    lst = f.readlines()
print(lst)
stud = {}
for s in lst:
    for i in s:
        if i.isdigit():
            stud.update({s[:-3]: i})
res = 0
for k, v in stud.items():
    res += int(v)
    if int(v) < 3:
        print(k)
print(res / len(stud))
print()
