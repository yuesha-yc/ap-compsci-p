"""
|-------------------------------------------------------------------------------
| creditcard.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 17, 2019
|
| This program determines the validity of a credit card number.
|
|  Valid credit card:   AMEX
|                       MASTERCARD
|                       VISA
|                       VALID
|
|  Invalid credit card: INVALID
|
|  Valid test values:
|  "378282246310005"    AMEX
|  "371449635398431"    AMEX
|  "5555555555554444"   MASTERCARD
|  "5105105105105100"   MASTERCARD
|  "4111111111111111"   VISA
|  "4012888888881881"   VISA
|  "6451962466988955"   VALID
|
|  Invalid test values:
|  "6176292929"         INVALID
|  "1234567890314"      INVALID
|
"""

def validate(digits):
    # YOUR CODE HERE
    products = 0
    summ = 0
    digitLen = len(digits)
    print(digitLen)
    for i in range(digitLen - 2, -1, -2):
        par = str(int(digits[i]) * 2)
        #print(par)
        for num in par:
            products += int(num)

    #print("")
    for i in range(digitLen - 1, -1, -2):
        #print(digits[i])
        summ += int(digits[i])
    validateNum = products + summ
    print(validateNum)
    if str(validateNum)[-1] == "0":
        if digitLen == 15 and (digits[0:1] == "34" or "37"): return "AMEX"
        elif (digitLen == 16 or digitLen == 13) and digits[0] == "4": return "VISA"
        elif digitLen == 16 and (digits.startswith("51") or digits.startswith("52") or digits.startswith("53") or digits.startswith("54") or digits.startswith("55")): return "MASTERCARD"
        
        else: return "VALID"

    else: return "INVALID"

result = validate("348605027629226")
print(result)

