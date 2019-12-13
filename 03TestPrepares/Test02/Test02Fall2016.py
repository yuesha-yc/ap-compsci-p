# FRQ, 34
def listinersect(alist, blist):
    commonlist = []
    for a in alist:
        if a in blist:
            commonlist.append(a)
    return commonlist

result = listinersect([1,3,5],[5,3])
print(result)

# FRQ, 35
def middle(L):
    mid = L[len(L)//2]
    return mid

sol = middle([1,2,3,4,5])
print(sol)

# FRQ, 36
"""
Same as Fall 2018
"""