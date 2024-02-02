print('найдем сумму ваших чисел')
sum = 0

while True:
    line = input(": ")
    if line == "":
        break
    if int(line) > 9:
        continue
    sum += int(line)
print(f"sum = {sum}")

# 2

# print("a**2")
# num = 1
#
# while num <= 10:
#     print(f"{num}^2 = {num**2}")
#     num += 1

# 3

# print("перемножим все четные от 1 до 125")
#
# num = 1
# res = 1
# while num < 125:
#     if num % 2 == 0:
#         res *= num
#     num += 1
# print(res)

# 5

print("печатаем числа от 1 до 100 кратные 7 в одну строку")

num = 1
while num < 100:
    if num % 7 == 0:
        print(num, end=" ")
    num += 1

print()
