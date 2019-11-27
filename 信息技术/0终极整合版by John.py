# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a tempora

author: John Qinrong Cui

"""
#1华氏转摄氏
a=float(input())
b=(a-32)/1.8
print(b)

#2矩形的面积
a=float(input())
b=float(input())
c=a*b
print(c)

#3A+B Problem
a=int(input())
b=int(input())
c=a+b
print(c)

#4时间转换1
a=int(input())
b=int(input())
c=int(input())
d=a*3600+b*60+c
print(d)

#5时间转换2
a=int(input())
b=a//3600
c=a%3600//60
d=a%3600%60
print(b,c,d)

#6分糖果
a=int(input())
b=int(input())
c=int(input())
d=a//3
e=(b+d)//3
f=(d+e+c)//3
g=d+e+f
h=e+f
print(g,h,f)

#7比大小1
a=int(input())
b=int(input())
if a<b:
    print(b)
else:
    print(a) 

#8比大小2
a=int(input())
b=int(input())
c=int(input())
if b>a:
    a=b
if c>a:
    a=c
print(a)

#9考试等级
a=int(input())
if 101>a>89:
    print('A')
elif 90>a>79:
    print("B")
elif 80>a>59:
    print('C')
elif -1<a<60:
    print('D')
else:
    print('wrong score')
    
#10平年闰年判定
a=int(input())
if a%100==0:
    if a%400==0:
        print('leap year')
    else:
        print('normal year')
else:
    b=a%4
    if b==0: 
        print('leap year')
    else:
        print('normal year')
    
#11晶晶的零花钱
p=int(input())
k=int(input())
t=int(input())
if p+k>t:
    print('happy')
else:
    print('unhappy')

#13模拟计算器
a=str(input())
b=float(input())
c=float(input())
if a=="+":
    d=b+c
elif a=='-':
    d=b-c
elif a=='*':
    d=b*c
elif a=='/':
    d=b/c
print(d)

#14身型鉴定
w=float(input())
h=float(input())
bmi=w/(h**2)
if bmi>=40:
    print('too fat')
elif 35<=bmi<40:
    print('normal fat')
elif 30<=bmi<35:
    print('fat')
elif 25<bmi<30:
    print('overweight')
elif 18<bmi<=25:
    print('very good')
elif bmi<18:
    print('too thin')
    
#15三角形判定
a=int(input())
b=int(input())
c=int(input())
if (a+b<c or a+c<b or b+c<a):
    print('impossible')
elif a==b==c:
    print('equilateral triangle')
elif (a==b or a==c or b==c):
    print('isosceles triangle')
elif(a+b>c and a+c>b and c+b>a):
    print('normal triangle')

#16水仙花数
a=int(input())
b=a%10
c=((a-b)/10)%10
d=(a-b-c*10)/100
e=d**3+b**3+c**3
if (a==e):
    print("yes")
else:
    print('no')


#18解的个数
a=int(input())
b=int(input())
c=int(input())
delta=b**2-4*a*c
if (a==0):
    print('one answer')
else:
    if (delta>0):
        print('two answers')
    elif (delta==0):
        print('two equal answers')
    else:
        print('no answer')

#20 打印奇数
n=int(input())
i=1
while (i<=n):
    print(i)
    i+=2    

#21 课堂点名
n=int(input())
for i in range(0,n):
    print("stu",i,end=" ",sep='')
    
#22 小明存钱1
day=int(input())
i=1
money=i
while (i<day):
    i+=1
    money+=i
print(money)

#23 数列积
n = int(input())
s = 1
for i in range (1,n+1,1):
    s *= i
print(s)

#24 调和级数
n = int(input())
s = 0
for i in range(1,n+1):
    s = s + 1/i
print(s)

#25 小明存钱2
k=int(input())
i=0
money=0
while (money<5888+k):
    i+=1
    money+=i
print(i)

#26 平方和
n=int(input())
s=0
i=0
while (i<n):
    i+=1
    s+=i**2
print(s)
    
#27 人口数
n=float(input())
p=float(input())
i=0
while (n<p):
    i+=1
    n+=n*0.005
print(i)
    
#28 人口增长
n=float(input())
p=float(input())
i=0
while (i<p):
    i+=1
    n+=n*0.005
print(n)

#29 折纸超珠峰
n=float(input())
h=float(input())
i=0
while (n<h):
    i+=1
    n+=n
print(i)

#30打印*号
n = int(input())
for i in range(1,n+1):
    print("*"*n)
    
#31打印*三角形
n = int(input())
for i in range(1,n+1):
    print("*"*i)   

#32打印*倒三角形
n = int(input())
for i in range(1,n+1):
    print("*"*i)   

#34点兵问题
a = int(input())
b = int(input())
c = int(input())
for i in range(100, 6, -1):
    if i % 3 == a and i % 5 == b and i % 7 == c:
        print(i)
        break
else:
    print("none")    

#36素数判定
n = int(input())
for i in range(n-1,1,-1):
    if n%i == 0:
        print("no")
        break
else:
    print("yes") 

#37统计人数
nan = 0
nv = 0
while True:
    a = int(input())
    if a == 1:
        nan += 1
    elif a == 2:
        nv += 1
    elif a == 0:
        break
    else:
        continue
print(nan+nv,nan,nv)

#42 鸡兔同笼
m = int(input())
n = int(input())
for ji in range(0,m+1):
    tu = m - ji
    if ji*2 + tu*4 == n:
        print(str(ji)+" "+str(tu))
#43 寻找质因数
def isprime(n): 
  for i in range(2, n):
    if n % i == 0:
      break
  else:
    return n 
  
num = int(input())
i = 1 
if num >= 2: 
  
  while i <= num: 
    i += 1
    if num % i == 0: 
      print(isprime(i),end=' ') 
      
      while num % i<1:
          num=num/i
          
     
      i = 1 
      pass 
    else:
      pass 

  
#44 幸运数字个数
'''
错误答案：
lm=int(input())
num=int(input())

digits=0 #判断数字位数
while num>0:
    num//10
    digits+=1

def islm(n): #判断此数位上有几个LM
    sum=0
    i=1
    while i<=num:
        i+=1
        if n/5==1:
            sum+=1
    return sum

while num>0:
    sum=islm(num)
    num//10
'''
#正确答案：
k=int(input())
n=int(input())
count = 0
for i in range(n+1):
    if i == 0 and i == k:
        count  += 1
    while( i // 10 >= 0 and i != 0):
        j = i % 10    
        if j == k:
            count  += 1
        i= i //10
print(count)

#45 小明买鸡
n=int(input())
q=0
for a in range(1,3*n+1,1):
    for i in range(0,int(n/5)+1,1):
        for j in range(0,a-i+1,1):
            if (i*5 + j*3 + int((a-i-j)/3)==n and (a-i-j)%3==0):
                q=q+1
print(q)

#96 奇偶数问题（未完成）
aList=[]
jiList=[]
ouList=[]
i=0
while i<10:
    aList.append(int(input()))
    i+=1
for i in range(0,10):
    if (aList[i])%2==0:
        ouList.append(aList[i])
    else:
        jiList.append(aList[i])
print(" ".join(repr(e) for e in jiList))
print(" ".join(repr(e) for e in ouList))

#97 开关灯问题
n,k=map(int,input().split())#不要在意，他可能会显示有invalid syntax但运行没问题
    # 使用正负号表示灯的状态
lights=[]
a=1
while a<=n:
    lights.append(a)
    a+=1
    
for i in range(1, k+1):
    for j in range(i-1, n, i):
        lights[j] = - lights[j]
    # 灯的状态存储在列表中
for k in range(len(lights)):
    if lights[k] > 0:
        lights[k] = 1
    else:
        lights[k] = 0
    #为了满足网站的司马要求，我们要把所有的0的位置检索出来，加入list  
find = 0
m=[i for i,v in enumerate(lights) if v==find]#把所有0的位置检索出来，注意这个从0开始记位
n=list(map(lambda x:x+1,m))#将所有list中元素+1
print(" ".join(repr(e) for e in n))#把所有，换成空格。把list转换为str。不然会和司马网站格式不匹配

#98 排名问题
n=int(input())
grade=[]
grade= list(map(int,input().split()))#输入list值，用split()空格分隔
#外层循环确定比较的轮数，x是下标，grade[x]在外层循环中代表grade中所有元素
k=int(input())
grade.append(k)
n+=1
for x in range(n-1):
   #内层循环开始比较
   for y in range(x+1,n):
      #grade[x]在for y 循环中是代表特定的元素，grade[y]代表任意一个grade任意一个元素。
      if grade[x]<grade[y]:
         #让grade[x]和grade列表中每一个元素比较，找出小的
         grade[x],grade[y]=grade[y],grade[x]
z=grade.index(k)
print(z+1)