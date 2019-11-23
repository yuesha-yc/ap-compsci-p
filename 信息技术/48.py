x = int(input())
y = int(input())
if x<y:
    smaller = x
else:
    smaller = y
for i in range(smaller,0,-1):
    if x%i==0 and y%i==0:
        print(i)
        break

