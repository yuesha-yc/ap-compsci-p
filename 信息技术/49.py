def gcd(x,y):
    if x < y:
        smaller = x
    else:
        smaller = y
    for i in range(smaller, 0, -1):
        if x % i == 0 and y % i == 0:
            solution = i
            break
    return solution

n = int(input())
g = int(input())
for i in range(n-1):
    m = int(input())
    g = gcd(g,m)

print(g)