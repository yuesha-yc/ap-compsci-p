a = int(input())
b = int(input())
c = int(input())

for i in range(100, 6, -1):
    if i % 3 == a and i % 5 == b and i % 7 == c:
        print(i)
        break
else:
    print("none")