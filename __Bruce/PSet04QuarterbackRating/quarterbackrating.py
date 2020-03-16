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
    a = (1.0*comps/attempts - 0.3) * 5
    b = (1.0*yards/attempts - 3) * 0.25
    c = 20.0 * tdowns/attempts
    d = 2.375 - (25.0 * picks/attempts)
    if (a > 2.375): a = 2.375
    if (b > 2.375): b = 2.375
    if (c > 2.375): c = 2.375
    if (d > 2.375): d = 2.375
    if (a < 0): a = 0
    if (b < 0): b = 0
    if (c < 0): c = 0
    if (d < 0): d = 0

    rating = ((a + b + c + d) / 6.0) * 100
    return rating

result = calculaterating(33, 26, 465, 5, 0)
print(result)

