import random
num = random.randint(3, 15)
num_2 = random.randint(3, 15)
print(('num', num) if num > num_2 else ('num_2', num_2))
