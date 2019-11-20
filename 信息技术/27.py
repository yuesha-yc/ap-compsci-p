n = float(input())
p = float(input())
y = 1
while n<p:
    n = n*(1+0.005)
    y += 1
print(y-1)
