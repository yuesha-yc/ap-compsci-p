nan = 0
nv = 0
while True:
    a = int(input())
    if a == 1:
        nan += 1
    elif a == 2:
        nv += 1
    elif a == 0:
        break
    else:
        continue

print(nan+nv,nan,nv)
