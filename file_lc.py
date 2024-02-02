# """"""
#
# import os
#
# print(os.getcwd())
# os.makedirs("test/test1")
# with open("test/test.txt", "w") as f:
#     f.write("#Hello\n World!!!")
# os.chdir("test")
# os.rename("test.txt", "test1/hello.md")
# print(os.getcwd())
# print(os.listdir("."))
# print(os.uname())
# os.chdir("..")
# os.remove("test/test1/hello.md")
# os.removedirs("test/test1")
#
# """Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список так, чтобы
# сначала шли числа по возрастанию, а потом слова по возрастанию их длинны."""
#
# with open("example.txt", "r") as f:
#     str = f.read()
#     lst = str.split("\n")
# print(lst)
# res1 = [int(i) for i in lst if i.isdigit()]
# res2 = [i for i in lst if i.isalpha()]
# print(sorted(res1) + sorted(res2, key=len))
#
# """Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
#  Окончанием ввода пусть служит пустая строка. В текстовом файле посчитать количество строк,
#   а также для каждой отдельной строки определить количество в ней символов."""
# with open("test2.txt", "a") as f:
#     while True:
#         str = input(": ")
#         if str == "":
#             break
#         else:
#             f.write(str + "\n")
# with open("test2.txt") as f:
#     text = f.readlines()
#     for i in text:
#         i = i.strip("\n")
#         print(f"{i} : {len(i)} char")

""" dz 
Есть список состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины,
а после слов цифры в порядке возрастания.
"""

lst = ["hjgjglhj", 65868, "lmmlklk", 6676, "sdsd", 7867]
text = sorted([i for i in lst if str(i).isalpha()], key=len)
number = sorted([i for i in lst if str(i).isdigit()])
# number=[]
# text=[]
# for i in lst:
#     if str(i).isalpha():
#         text.append(i)
#     else:
#         number.append(i)
number = [str(i) for i in number]
with open("test3.txt", "a") as f:
    f.writelines(f"{' '.join(text)} {' '.join(number)}\n")

