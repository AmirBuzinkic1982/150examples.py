'''nums=[]

num1=int(input("Enter the first number: "))
nums.append(num1)
print(nums)
num2=int(input("Enter the second number: "))
nums.append(num2)
print(nums)
num3=int(input("Enter a third number: "))
nums.append(num3)
print(nums)

answer=input("Do you still want that last number in your list y/n: ")

if answer=="n":
    nums.remove(num3)
    print(nums)'''

nums=[]
count=0

while count<3:
    num=int(input("Enter a number"))
    nums.append(num)
    print(nums)
    count=count+1

lastnum=input("Do you want the last number saved y/n: ")
if lastnum=="n":
    nums.remove(num)
    print(nums)