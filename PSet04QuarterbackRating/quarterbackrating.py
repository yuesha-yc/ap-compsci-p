"""
|-------------------------------------------------------------------------------
| quarterbackrating.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 22, 2019
|
| This program determines the passer rating of an NFL quarterback.
|
"""

def calculaterating(attempts, comps, yards, tdowns, picks):
    # YOUR CODE HERE
    a_ = (1.0 * comps / attempts - 0.3) * 5
    b_ = (1.0 * yards / attempts - 3) * 0.25
    c_ = 20.0 * tdowns / attempts
    d_ = 2.375 - (25.0 * picks / attempts)
    if 0 <= a_ <= 2.375:
        a = a_
    elif a_ < 0:
        a = 0
    else:
        a = 2.375

    if 0 <= b_ <= 2.375:
        b = b_
    elif b_ < 0:
        b = 0
    else:
        b = 2.375

    if 0 <= c_ <= 2.375:
        c = c_
    elif c_ < 0:
        c = 0
    else:
        c = 2.375

    if 0 <= d_ <= 2.375:
        d = d_
    elif d_ < 0:
        d = 0
    else:
        d = 2.375

    rating = ((a + b + c + d) / 6.0) * 100

    return rating

result = calculaterating(35, 26, 235, 2, 1)
print(result)

