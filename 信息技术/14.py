w = float(input())
h = float(input())
bmi = w/(h**2)

if bmi<18:
    print('too thin')
elif 18<=bmi<=25:
    print('very good')
elif 25<bmi<30:
    print('overweight')
elif 30<=bmi<35:
    print('fat')
elif 35<=bmi<40:
    print('normal fat')
else:
    print('too fat')
