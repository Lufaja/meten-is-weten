print('Vul een getal in voor a en b')
a = input('a = ')
b = input('b = ')

if a > b:
    Max = a
    print('a is het grootste getal: ' + str(Max))
elif a < b:
    
    Min = a
    print('a is het kleinste getal: ' + str(Min))
else:
    print("a en b zijn even groot")