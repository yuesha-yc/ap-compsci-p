"""
|-------------------------------------------------------------------------------
| coinchange.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 11, 2019
|
| This program determines the the minimum number of coins for a particular value.
|
"""

def minimumcoins(cents):
    # YOUR CODE HERE
    ans = 0
    while cents >= 25:
        cents -= 25
        ans = ans + 1
    while cents >= 10:
        cents -= 10
        ans = ans + 1
    while cents >= 5:
        cents -= 5
        ans = ans + 1
    while cents >= 1:
        cents -= 1
        ans = ans + 1

    return(ans)
result = minimumcoins(2300)
print(result)
