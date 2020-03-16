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
    downPayment = totalcost * 0.25
    savedMoney = 0
    monthSpend = 0
    monthlySalary = annualsalary / 12

    while (1):
        
        savedMoney += ((savedMoney * 0.04) / 12)

        if (monthSpend % 6) == 0 and monthSpend != 0:
            monthlySalary = (monthlySalary * (1 + payraise))
        
        savedMoney += (monthlySalary * percentsaved)

        monthSpend += 1
        if (savedMoney >= downPayment): break

    return monthSpend

result = savingsduration(120000, 0.05, 500000, 0.03)
print(result)

