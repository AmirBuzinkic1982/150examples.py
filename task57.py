import random

num=random.randint(1,10)
print(num)

correct=False

while correct==False:
    guess=int(input("Enter a number: "))
    if guess>num:
        print("Number is too high")
    elif guess<num:
        print("Number is too low")
    elif guess==num:
        correct=True
    
        


