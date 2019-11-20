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
    length = len(digits)
    sum = 0
    if length == 15 and (digits.startswith("37") or digits.startswith("34")):
        for i in range(1,length-1,2):
            each = str(int(digits[i])*2)
            for j in range(0,len(each)):
                sum += int(each[j])
        for k in range(0,length+1,2):
            sum += int(digits[k])
        if str(sum)[-1] == "0":
            solution = "AMEX"


    elif length == 16 and (digits.startswith("51") or digits.startswith("52") or digits.startswith("53") or digits.startswith("54") or digits.startswith("55")):
        for i in range(0,length-1,2):
            each = str(int(digits[i])*2)
            for j in range(0,len(each)):
                sum += int(each[j])
        for k in range(1,length,2):
            sum += int(digits[k])
        if str(sum)[-1] == "0":
            solution = "MASTERCARD"

    elif length == 16 and digits.startswith("4"):
        for i in range(0,length-1,2):
            each = str(int(digits[i])*2)
            for j in range(0,len(each)):
                sum += int(each[j])
        for k in range(1,length,2):
            sum += int(digits[k])
        if str(sum)[-1] == "0":
                solution = "VISA"


    elif length == 13 and digits.startswith("4"):
        for i in range(1,length-1,2):
            each = str(int(digits[i])*2)
            for j in range(0,len(each)):
                sum += int(each[j])
        for k in range(0,length+1,2):
            sum += int(digits[k])
        if str(sum)[-1] == "0":
                solution = "VISA"

    else:
        if length%2 == 1:
            for i in range(1, length-1, 2):
                each = str(int(digits[i]) * 2)
                for j in range(0, len(each)):
                    sum += int(each[j])
            for k in range(0, length+1, 2):
                sum += int(digits[k])
            if str(sum)[-1] == "0":
                solution = "VALID"
            else:
                solution = "INVALID"

        elif length%2 == 0:
            for i in range(1, length-1, 2):
                each = str(int(digits[i]) * 2)
                for j in range(0, len(each)):
                    sum += int(each[j])
            for k in range(0, length, 2):
                sum += int(digits[k])
            if str(sum)[-1] == "0":
                solution = "VALID"
            else:
                solution = "INVALID"

    return solution


result = validate("378282246310005")
print(result)

