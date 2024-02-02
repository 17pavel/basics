from random import randint

number = randint(100, 999)
a = number // 100
b = (number // 10) % 10
c = number % 10
suma = a + b + c
print("случайное трехзначное число:", number)
print("сумма цифр:", suma)
