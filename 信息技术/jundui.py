n = int(input())

for i in range(1,n+1):
    pass
    for j in range(1,n+1):
        print(i*10+j, end=" ")
    print("")


# sanjiao
for i in range(1,n+1):
    pass
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

#daosanjiao
for i in range(n,0,-1):
    pass
    for j in range(1,i+1):
        print(j, end=" ")
    print("")

# fansanjiao
for i in range(1,n+1):
    j = n - i
    print(j*" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print("")
