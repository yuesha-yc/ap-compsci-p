#打印矩阵
n = int(input())
for j in range(1,n+1):
    if j % 2 == 1:
        for i in range(n*(j-1)+1,j*n+1):
            print(i, end=" ")
        print()
    else:
        for i in range(n*j,n*(j-1),-1):
            print(i, end=" ")
        print()