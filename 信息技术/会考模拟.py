#81
a = float(input())
n = 2035*(1+a)**5
print(n)

#82
mb = float(input())
if mb <= 700:
    s = 40
else:
    s = 40 + (mb-700)*0.29
print(s)

#83
n = float(input())
h = 0.0001
i = 0
while h < n:
    h *= 2
    i += 1
print(i)

#84
n = int(input())
c = 0
i=1
while c<n:
    if i%7==0 or i%10==7:
        print(i)
        c += 1
    i+=1

#85
s = int(input())
if s < 200:
    f = s
else:
    f = s - (s//200)*20
print(f)

#86
a = int(input())
min = a//60
sec = a%60
print(str(min) + " " + str(sec))

#87
for num in range(100,1000):
    si = str(num)
    if num == int(si[0])**3 + int(si[1])**3 + int(si[2])**3:
        print(num)

#88
a = int(input())
b = int(input())
left = 150 - a*13 - b*4
print(left)

#89
n = int(input())
best = 999
for i in range(0,n):
    a = int(input())
    if a<best:
        best = a
print(best)

#90
p = float(input())
if p <= 500:
    print(p)
elif 500<p<=2000:
    print(p*0.9)
else:
    print(p*0.85)