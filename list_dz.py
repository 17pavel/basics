# str = 'В строке, удалить знаки препинания, пробелы.'
# a = list(str)
# for i in a:
#     if ord(i) < 192:
#         a.remove(i)
#         print(i, ord(i))
# print(a)

lst = [15, 48, 'hello', 6, 19, 'world']
print(lst)
s = 0
glas = 0
sogl = 0

for i in lst:
    if type(i) is int:
        if i % 2 != 0:
            ind = lst.index(i)
            lst[ind] = 1
        else:
            for x in str(i):
                s += int(x)
            print(i, 'suma', s)
            s = 0
    if type(i) is str:
        for k in list(i):
            if k in ['e', 'y', 'u', 'i', 'o', 'a']:
                glas += 1
            else:
                sogl += 1
        print(f" word {i}: glas {glas}, sogl {sogl}")
        glas = 0
        sogl = 0
print(lst)
