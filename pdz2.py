from random import choice

chislo_1 = int(input("vvedide chislo_1 ot 1 do 36: "))
chislo_2 = int(input("vvedide chislo_2 ot 1 do 36: "))
chislo_3 = int(input("vvedide chislo_3 ot 1 do 36: "))
chislo_4 = int(input("vvedide chislo_4 ot 1 do 36: "))
chislo_5 = int(input("vvedide chislo_5 ot 1 do 36: "))
chislo_6 = int(input("vvedide chislo_6 ot 1 do 36: "))

lst = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
]

rand_chislo_1 = choice(lst)
lst.remove(rand_chislo_1)

rand_chislo_2 = choice(lst)
lst.remove(rand_chislo_2)

rand_chislo_3 = choice(lst)
lst.remove(rand_chislo_3)

rand_chislo_4 = choice(lst)
lst.remove(rand_chislo_4)

rand_chislo_5 = choice(lst)
lst.remove(rand_chislo_5)

rand_chislo_6 = choice(lst)
lst.remove(rand_chislo_6)

lst_2 = [
    rand_chislo_1,
    rand_chislo_2,
    rand_chislo_3,
    rand_chislo_4,
    rand_chislo_5,
    rand_chislo_6,
]
print("vash vybor: ", [chislo_1, chislo_2,
      chislo_3, chislo_4, chislo_5, chislo_6])
print("resultat loterei: ", lst_2)
