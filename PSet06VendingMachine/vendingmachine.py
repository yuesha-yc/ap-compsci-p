"""
|-------------------------------------------------------------------------------
| vendingmachine.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 13, 2019
|
| This program simulates a simple change maker for a vending machine.
|
"""

def dispensechange(quarters, dimes, nickels, cost, payment):
    # YOUR CODE HERE
    change = payment - cost
    num = 0
    while change >= 25 and quarters > 0:
        change -= 25
        num += 1
        quarters -= 1

    while change >= 10 and dimes > 0:
        change -= 10
        num += 1
        dimes -= 1

    while change >= 5:
        change -= 5
        num += 1
        nickels -= 1

    return num


result = dispensechange(5, 5, 5, 160, 200)
print(result)

