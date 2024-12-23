num1=int(input("Enter a number:  "))
total=num1
again="y"



while again =="y":
    num2=int(input("Enter another number: "))
    total=total+num2
    again=input("Do you want to add another number: ")
    print("The total is",total)



#the one below is correct as well
'''
    num=int(input("Enter a number: "))
num1=int(input("Enter another number: "))
total=num+num1
answer=input("Do you want to add another number y/n: ")

while answer=="y":
    
    num=int(input("Enter another number: "))
    answer=input("Do you want to add another number y/n: ")
print(total)'''


