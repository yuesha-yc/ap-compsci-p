m = int(input())
n = int(input())

for ji in range(0,m+1):
    tu = m - ji
    if ji*2 + tu*4 == n:
        print(str(ji)+" "+str(tu))