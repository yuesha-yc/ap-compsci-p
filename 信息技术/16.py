water = str(input())

first = int(water[0])
second = int(water[1])
third = int(water[2:])

if (first**3 + second**3 + third**3)==int(water):
    print('yes')
else:
    print('no')
