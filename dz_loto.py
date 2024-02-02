import random

number_user = int(input('vvedite chislo ot 1 do 9: '))

number_random = random.randint(1, 9)

print('number_random = ', number_random)
if number_user < 1 or number_user > 9 :
    print('poprobuite eche ras')

elif number_random == number_user:
    print('you win!!!')

else :
    print ('vi proigrali')
