"""
|-------------------------------------------------------------------------------
| waterbilling.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 08, 2019
|
| This program determines the amount of a customer's water bill.
|
"""

def calculatebill(customer, begin, end):
    # YOUR CODE HERE
    volume = (end-begin)/10
    if customer == "residential":
        rate = 5 + 0.0005*volume
    elif customer == "commercial":
        if volume<=40000:
            rate = 1000
        else:
            rate = 1000 + (volume-40000)*0.00025
    elif customer == "industrial":
        if volume <= 40000:
            rate = 1000
        elif 40000<=volume<=80000:
            rate = 2000
        else:
            rate = 3000 + (volume-80000)*0.00025
    else:
        rate = "DNE"
    return rate

result = calculatebill("residential", 444400003, 444400135)
print(result)

