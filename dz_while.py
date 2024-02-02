print('поиграем в рулетку')
from random import randint

numbers = randint(1,10)
color = randint(1,2)
r = 0
while r < 5:
    num = int(input('выберите число от 1 до 10:'))
    col = int(input('введите 1(красное) или 2(черное):'))
    if num == numbers and col == color:
        print('вы выиграли')
        break
    else:
        print('не повезло')
    r += 1
else:
    print(f'выпало {numbers} , {color}')