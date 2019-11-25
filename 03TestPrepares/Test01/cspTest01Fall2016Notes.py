# Question 22
import math
def circlearea(radius):
    a = math.pi*radius**2
    return a

print(circlearea(2))

# Question 23
def totalseconds(hours, minutes, seconds):
    total = hours*3600 + minutes*60 + seconds
    return total

print(totalseconds(7, 21, 37))

# Question 24
def temperature(fahrenheit):
    celsius = (5/9)*(fahrenheit-32)
    return celsius

print(temperature(1000))

# Question 25
def grosspay(hours, rate):
    if hours<=40:
        pay = hours*rate
    else:
        pay = 40*rate+(hours-40)*rate*1.5
    return pay

print(grosspay(50,10))

# Question 26
def triangle(a,b,c):
    if a+b<=c or a+c<=b or b+c<=a:
        z = False
    else:
        z = True
    return z

print(triangle(5,6,10))

#
