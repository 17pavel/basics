mesac = int(input('vvedite mesec: '))
den = int(input('vvedite den: '))
5
if 1 > mesac > 12 or 1 > den > 31:
    print('nevernii vvod')

elif mesac == 4:
    if den <= 20:
        print('oven')
    else:
        print('telec')

elif mesac == 5:
    if den <= 21:
        print('telec')
    else:
        print('bliznety')

elif mesac == 6:
    if den <= 21:
        print('bliznety')
    else:
        print('rak')

elif mesac == 7:
    if den <= 22:
        print('rak')
    else:
        print('lev')

elif mesac == 8:
    if den <= 21:
        print('lev')
    else:
        print('deva')

else:
    print('nuzno dopisat cod samomu')