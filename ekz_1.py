# # 1
# print("с клавы ввод текста, определить: кол. глас. и согл.")
#
# str = input(": ")
# gl_num = 0
# sogl_num = 0
# for i in str:
#     if i in "eyuioa":
#         gl_num += 1
#     else:
#         sogl_num += 1
# print(f"gl_num: {gl_num}, sogl_num: {sogl_num}")
#
# # 2
#
# print("найти среднее из трех чисел")
#
# num_1 = int(input("num_1: "))
# num_2 = int(input("num_2: "))
# num_3 = int(input("num_3: "))
#
# if num_1 < num_3:
#     if num_2 >= num_3:
#         print("res ", num_3)
#     else:
#         if num_2 < num_1:
#             print("res ", num_1)
#         else:
#             print("res ", num_2)
# else:  # num_1 >= num_3
#     if num_2 >= num_1:
#         print("res", num_1)
#     else:
#         if num_2 <= num_3:
#             print("res: ", num_3)
#         else:
#             print("res: ", num_2)
# # 3
#
# print("list[7],if chet>nechet print sum else print 1*3*6")
#
# lst = [345, 534, 786, 45, 32, 57, 65]
#
# n_chet = 0
# n_nechet = 0
#
# for i in lst:
#     if i % 2 == 0:
#         n_chet += 1
#     else:
#         n_nechet += 1
# if n_chet < n_nechet:
#     print("mult: ", lst[0]*lst[2]*lst[5])
# else:
#     print("sum: ", sum(lst))
#
# # 4
# from random import randint
# num = input("num: ")
# print("reverse: ", num[::-1])
#
# # 5
#
#
# lst = [randint(1, 99) for i in range(10)]
# print(lst)
# print("sum: ", sum(lst))
# mult = 1
# for i in lst:
#     mult *= i
# print("mult: ", mult)
#
# # 6
#
# str = input("del space,  polyndrom?: ")
#
# str = str.replace(" ", "")
# print(str)
# if str == str[::-1]:
#     print("polyndrom")

# # 7
#
# len = int(input("len_lst: "))
# lst = [None]*len
#
# print(lst)
# for i, n in enumerate(lst):
#     num = int(input("input num: "))
#     lst[i] = num
# print(lst)
# poz = int(input("input pozition:"))
# number = int(input("input number:"))
# lst.insert(poz-1, number)
# print(lst)
#
# # 8
#
# import string
# str = input(": ")
# lst = str.split()
# print("len: ", len(lst))
#
# # 9
#
# import string
# str = input("heLLoo: ")
# res = 0
# for i, l in enumerate(str):
#     if l in string.ascii_uppercase:
#         if str[i] == str[i-1]:
#             res += 1
# print(res)

# 10

from random import randint

lst = [randint(1000, 9999) for i in range(10)]
res = 0
for num in lst:
    for i in str(num):
        if int(i) == 1:
            res += 1
print(lst)
print(f"count 1 : {res}")
