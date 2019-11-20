a = int(input())
b = int(input())
c = int(input())

if a == 0:
    print('one answer')
else:
    if (b**2-4*a*c) > 0:
        print('two answers')
    elif (b**2-4*a*c) == 0:
        print('two equal answers')
    else: print('no answer')
