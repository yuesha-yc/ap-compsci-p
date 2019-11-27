n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        product = i*j
        p = str(product)
        print(str(j)+"*"+str(i)+"="+p,end=" ")
    print()

