"""
|-------------------------------------------------------------------------------
| downpayment.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 18, 2019
|
| This program determines the number of months required for a down payment.
|
"""

def savingsduration(annualsalary, percentsaved, totalcost, payraise):
    # YOUR CODE HERE
    downpayment = totalcost*0.25
    monthsalary = annualsalary/12.0
    saving = 0
    rate = 0.04
    months = 0
    while saving < downpayment:
        months += 1
        saving = saving*(1+rate/12.0) + percentsaved*monthsalary
        if months%6 == 0:
            monthsalary = monthsalary*(1+payraise)

    return months


result = savingsduration(120000, 0.05, 500000, 0.03)
print(result)

