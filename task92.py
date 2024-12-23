from array import*
import random

num1=array('i',[])
num2=array('i',[])

for i in range(0,3):
    number=int(input("Enter a number: "))
    num1.append(number)


for i in range(0,5):
    num=random.randint(0,100)
    num2.append(num)

num1.extend(num2)

num1=sorted(num1)

for i in num1:
    print(num1)