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
    charge = payment - cost
    ans = 0
    charge_quarters = charge // 25
    if charge_quarters > quarters:
        charge_quarters = quarters
    charge = charge - (25 * charge_quarters)

    charge_dimes = charge // 10
    if charge_dimes > dimes:
        charge_dimes = dimes
    charge = charge - (10 * charge_dimes)

    charge_nickels = charge // 5
    if charge_nickels > nickels:
        charge_nickels = nickels
    charge = charge - (5 * charge_nickels)

    ans = charge_dimes + charge_nickels + charge_quarters
    
    return ans

result = dispensechange(2, 287, 157, 5285, 8570)
print(result)

