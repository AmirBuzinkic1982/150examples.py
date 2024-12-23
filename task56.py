import random

'''num=random.randint(1,10)
print(num)

guess=int(input("Guess a number: "))

while guess != num:
    guess=int(input("Enter a number: "))'''

num=random.randint(1,10)

correct=False

while correct==False:
    guess=int(input("Enter a number: "))
    if guess==num:
        correct=True