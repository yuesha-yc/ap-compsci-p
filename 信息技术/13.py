operator = input()
a = float(input())
b = float(input())

if operator == '+':
    r = a+b
elif operator == '-':
    r = a-b
elif operator == '*':
    r = a*b
else:
    r = a/b
print(r)
