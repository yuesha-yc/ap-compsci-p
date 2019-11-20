a = int(input())
b = int(input())
c = int(input())

if a+b>c and b+c>a and a+c>b:
    if a == b and b == c:
        print('equilateral triangle')
    elif a == b or a == c or b == c:
        print('isosceles triangle')
    else:
        print('normal triangle')
else:
    print('impossible')
